from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.views import get_random_string
from .models import OnlineGameToken, OnlinePlayer,OnlineGame


def room(request, room_name,player=""):
    return render(request, 'room.html', {
        'room_name': room_name,
        "player":player
    })
@api_view(["POST"])

# requirements : colorId,name
def createGame(request):
    data = request.data
    game = OnlineGame()
    if "colorId" in data:
        colorId = data["colorId"]
        name =""
        if "name" in data:
            name = data["name"]
        if colorId>-1 and colorId<4:
            player = game.initialize(colorId,name)
            key = get_random_string(20)
            OnlineGameToken.objects.create(key=key,game=game)
            return Response({
                "status":0,
                "player":player,
                "game":key
            })
    return Response({"status":1,"message":"initial color"})

# requirements : colorId ,gameToken,name
@api_view(["POST"])
def joinGame(request):
    data = request.data
    if "colorId" in data and "token" in data:
        colorId = data["colorId"]
        if colorId<=-1 and colorId>=4:
            return Response({"status":-1 ,"message":"color unavailable"})
        try:
            game =OnlineGameToken.objects.get(key=data["token"]).game
        except:
            return Response({"status":1 ,"message":"Game unavailable"})
        for p in game.players.all():
            if p.colorId == colorId:
                return Response({"status":-1 ,"message":"color unavailable"})
        player = OnlinePlayer(colorId=colorId)
        name =""
        if "name" in data:
            name = data["name"]
        player.initialize(game,name=name)
        return Response({"status":0 ,"token":player.token})
    return Response({"status":-1 ,"message":"invalid data"})




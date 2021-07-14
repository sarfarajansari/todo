from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.views import get_random_string
from .models import OnlineGameToken, OnlinePlayer, OnlineGame, Message,Step
from . serializers import MessageSerializer, GameSerializer


# requirements : colorId,name
@api_view(["POST"])
def create(request):
    data = request.data
    game = OnlineGame()
    if "colorId" in data:
        colorId = data["colorId"]
        name = ""
        if "name" in data:
            name = data["name"]
        if colorId > -1 and colorId < 4:
            player = game.initialize(colorId, name)
            key = get_random_string(20)
            OnlineGameToken.objects.create(key=key, game=game)
            return Response({
                "status": 0,
                "player": player,
                "game": key
            })
    return Response({"status": 1, "message": "initial color"})

# requirements : colorId ,gameToken,name


@api_view(["POST"])
def join(request):
    data = request.data
    if "colorId" in data and "token" in data:
        colorId = data["colorId"]
        if colorId <= -1 and colorId >= 4:
            return Response({"status": -1, "message": "color unavailable"})
        try:
            game = OnlineGameToken.objects.get(key=data["token"]).game
        except:
            return Response({"status": 1, "message": "Game unavailable"})
        for p in game.players.all():
            if p.colorId == colorId:
                return Response({"status": -1, "message": "color unavailable"})
        player = OnlinePlayer(colorId=colorId)
        name = ""
        if "name" in data:
            name = data["name"]
        player.initialize(game, name=name)
        return Response({"status": 0, "token": player.token})
    return Response({"status": -1, "message": "invalid data"})


@api_view(["GET"])
def Connect(request, gtoken, ptoken):
    try:
        game = OnlineGameToken.objects.get(key=gtoken).game
        player = OnlinePlayer.objects.get(token=ptoken, game=game)
    except:
        return Response({"status": -1, "message": "invalid game"})

    player.active = True
    player.save()


    game.save()
    Message.objects.create(name="log", text=player.name +
                           " joined the game!", game=game)
    for p in game.players.all():
        p.refresh = True
        p.updateGame = False
        p.save()

    messages = MessageSerializer(game.msgs.all(), many=True).data
    gameData = GameSerializer(game).data
    return Response({
        "messages": messages,
        "game": gameData,
        "player": player.colorId,
        "status": 0,
    })


@api_view(["GET"])
def Disconnect(request, gtoken, ptoken):
    try:
        game = OnlineGameToken.objects.get(key=gtoken).game
        player = OnlinePlayer.objects.get(token=ptoken, game=game)
    except:
        return Response({"status": -1, "message": "invalid game"})
    player.active = False
    player.save()
    Message.objects.create(name="log", text=player.name + " left!", game=game)
    for p in game.players.all():
        p.updateMessage = True
        p.refresh = True
        p.save()

    return Response({})


@api_view(["GET"])
def updateMessage(request, gtoken, ptoken):
    try:
        game = OnlineGameToken.objects.get(key=gtoken).game
        player = OnlinePlayer.objects.get(token=ptoken)
    except:
        return Response({"status": -1, "message": "invalid game"})
    if player.updateMessage:
        player.updateMessage = False
        player.save()
        gameMessages = game.msgs.all()
        if len(gameMessages)>30:
            gameMessages = list(list(gameMessages)[-29:])
        messages = MessageSerializer(gameMessages, many=True).data
        data = {
            "messages": messages,
            "status": 0
        }
        return Response(data)
    return Response({
        "status": 1,
    })


@api_view(["GET"])
def updateGame(request, gtoken, ptoken):
    try:
        game = OnlineGameToken.objects.get(key=gtoken).game
        player = OnlinePlayer.objects.get(token=ptoken)
    except:
        return Response({"status": -1, "message": "invalid game"})
    if player.updateGame or player.refresh:
        needplay = player.updateGame
        if player.refresh:
            player.refresh = False
        if player.updateGame:
            player.updateGame = False
        player.save()

        data = {
            "game": GameSerializer(game).data,
            "status": 0,
            "play":needplay
        }
        return Response(data)
    return Response({
        "status": 1,
    })


@api_view(["POST"])
def sendMessage(request):
    data = request.data
    if "message" in data and "name" in data and "token" in data:
        try:
            game = OnlineGameToken.objects.get(key=data["token"]).game
        except:
            return Response({"status": 1, "message": "invalid game"})
        Message.objects.create(
            game=game, text=data["message"], name=data["name"])
        for p in game.players.all():
            p.updateMessage = True
            p.save()
        return Response({"status": 0})
    return Response({"status": 1, "message": "invalid message"})


@api_view(["POST"])
def play(request, gtoken, ptoken):
    data = request.data
    try:
        game = OnlineGameToken.objects.get(key=gtoken).game
        thisplayer = OnlinePlayer.objects.get(token=ptoken)
    except:
        return Response({"status": -1, "message": "invalid game"})
    game.winner = data["winner"]
    game.ended = data["ended"]
    game.loser = data["loser"]
    game.runnerup1 = data["runnerup1"]
    game.runnerup2 = data["runnerup2"]
    game.turn = data["turn"]
    game.winnerId = data["winnerId"]
    game.winner = data["winner"]
    game.lastTurn = thisplayer.colorId
    game.dice = data["dice"]
    
    game.old.y = data["old"][0]
    game.old.x = data["old"][1]
    game.old.save()

    for step in game.steps.all():
        step.delete()
    
    for step in data["steps"]:
        Step.objects.create(y=step[0],x=step[1],game=game)

    game.save()

    for p in game.players.all():
        for player in data["players"]:
            print(player)
            if p.colorId == player["colorId"]:
                p.active = True
                if p.id!=thisplayer.id:
                    p.updateGame= True
                p.save()

                for c in p.coordinates.all():
                    for cdata in player["coordinates"]:
                        if c.number == cdata["number"]:
                            c.x = cdata["x"]
                            c.y = cdata["y"]
                            c.initial = cdata["initial"]
                            c.reached = cdata["reached"]
                            c.save()
                            break
                break
    return Response({})
            



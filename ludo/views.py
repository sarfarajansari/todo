from .models import Game,GameToken,ChatMessage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GameSerializer,MessageSerializer
from store.views import get_random_string


def add_message_status(status,data, message=""):
    data["status"] = status
    if message:
        data["message"] = message
    return data

def get_index(players,colorId):
    for i in range(len(players)):
        if players[i]["colorId"] == colorId:
            return i
    return False


@api_view(["POST"])
def newGame(request):
    if "listPlayers" in request.data:
        game = Game(No_of_players=len(request.data["listPlayers"]))
        if "names" in request.data:
            game.initialize(request.data["listPlayers"],request.data["names"])
        else:
            game.initialize(request.data["listPlayers"])
        key =get_random_string(20)
        token = GameToken(key = key,game=game)
        token.save()
        data = add_message_status(0,{"token":key})
        return Response(data)
    return Response(add_message_status(1,{},"Could not start game. Please retry!"))

@api_view(["GET"])
def Reinitialize(request,token):
    try:
        game = GameToken.objects.get(key=token).game
        game.reinitialize()
        data = add_message_status(0,GameSerializer(game).data)
        return Response(data)
    except:
        return Response({"status":1,"message":"could not restart game"})

@api_view(["GET","POST"])
def getGame(request,token):
    try:
        game = GameToken.objects.get(key=token).game
        data = add_message_status(0,GameSerializer(game).data)
        data["rolled"]=False
        data["old"]=[0,0]
        data["dice"]=4
        data["steps"]=[]
        return Response(data)
    except:
        return Response({"status":1,"message":"could not restart game"})
        



@api_view(["POST"])
def Play(request,token):
    try:
        game = GameToken.objects.get(key=token).game
    except:
        return Response({"status":1,"message":"invalid game"})
    data = request.data
    if "ended" in data and "loser" in data and "players" in data and "runnerup1" in data and "runnerup2" in data and "turn" in data and "winner" in data and "winnerId" in data:
        game.ended = data["ended"]
        game.loser = data["loser"]
        game.runnerup1 = data["runnerup1"]
        game.runnerup2 = data["runnerup2"]
        game.turn = data["turn"]
        game.winnerId = data["winnerId"]
        game.winner = data["winner"]
        game.save()
        for player in game.players.all():
            for c in player.coordinates.all():
                coordinate = data["players"][get_index(data["players"],player.colorId)]["coordinates"][c.number]
                c.x = coordinate["x"]
                c.y = coordinate["y"]
                c.initial= coordinate["initial"]
                c.reached= coordinate["reached"]
                c.save()

        return Response(add_message_status(0,{}))
    return Response(add_message_status(1,{}))

@api_view(["POST"])
def nextplayer(request,token):
    try:
        game = GameToken.objects.get(key=token).game
    except:
        return Response({"status":1,"message":"invalid game"})
    game.get_next_turn()
    data = add_message_status(0,GameSerializer(game).data)
    data['rolled']=False
    data["steps"]=[]
    return Response(data)



@api_view(["GET"])
def test(request):
    game = Game.objects.first()
    return Response(add_message_status(1,GameSerializer(game).data,"this is test"))

@api_view(["GET"])
def getMessage(request,token):
    try:
        game = GameToken.objects.get(key=token).game
    except:
        return Response({"status":1,"message":"invalid game"})
    
    messages =MessageSerializer(game.msgs.all(),many=True).data
    return Response({"status":0,"data":messages,"type":1})

@api_view(["POST"])
def sendMessage(request):
    data = request.data
    if "message" in data and "token" in data:
        try:
            game = GameToken.objects.get(key=data["token"]).game
        except:
            return Response({})
        ChatMessage.objects.create(game=game,text =data["message"])
        return Response({})
    return Response({})

        





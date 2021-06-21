from .models import Game,GameToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GameSerializer
from store.views import get_random_string


def add_message_status(status,data, message=""):
    data["status"] = status
    if message:
        data["message"] = message
    return data

@api_view(["POST"])
def newGame(request):
    if "listPlayers" in request.data:
        game = Game(len(request.data["listPlayers"]))
        if "names" in request.data:
            game.initialize(request.data["listPlayers"],request.data["names"])
        else:
            game.initialize(request.data["listPlayers"])
        token = GameToken(key = get_random_string(20),game=game)
        data =GameSerializer(game).data
        data["token"] = token
        data = add_message_status(0,data)
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
        



@api_view(["POST"])
def Play(request,token):
    try:
        game = GameToken.objects.get(key=token).game
    except:
        return Response({"status":1,"message":"invalid game"})
    data = request.data
    if "colorId" in data and "number" in data:
        try:
            c = game.players.get(colorId=data["colorId"]).coordinates.get(number=data["number"])
        except:
            return Response(add_message_status(1,GameSerializer(game).data))
        if "step" in data:
            if "fake" in data.keys():
                stepped = c.step(data["step"],data["fake"])
            else:
                stepped = c.step(data["step"],False)
            if stepped and data["step"]==6:
                rolled = False
            else:
                if not "fake" in data.keys():
                    rolled = not c.player.update_turn(stepped)
                else:
                    rolled = False
            data = add_message_status(0,GameSerializer(game).data)
            data["rolled"] = rolled
            return Response(data)
        elif "initialize" in data:
            if data["initialize"]:
                c.initialize()
                return Response(add_message_status(0,GameSerializer(game).data))
    return Response(add_message_status(1,GameSerializer(game).data))

@api_view(["POST"])
def nextplayer(request,token):
    try:
        game = GameToken.objects.get(key=token).game
    except:
        return Response({"status":1,"message":"invalid game"})
    game.get_next_turn()
    data = add_message_status(1,GameSerializer(game).data)
    data['rolled']=False
    return Response(data)



@api_view(["GET"])
def test(request):
    game = Game.objects.first()
    return Response(add_message_status(1,GameSerializer(game).data,"this is test"))

        





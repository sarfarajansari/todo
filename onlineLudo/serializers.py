from rest_framework import serializers
from .models import OnlineGame as Game,Coord as Coordinates,OnlinePlayer as Player,Message,LastPlayed

class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields =["x","y","number","initial","reached",]


class PlayerSerializer(serializers.ModelSerializer):
    coordinates = CoordinateSerializer(many=True)
    class Meta:
        model = Player
        fields =["name","turn","color","colorId","complete","coordinates","onground","singleturn","active","host","updateMessage","updateGame"]


class LastPlayedSerializer(serializers.ModelSerializer):
    class Meta:
        model=LastPlayed
        fields ="__all__"
class GameSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)
    lastplayed = LastPlayedSerializer()
    class Meta:
        model = Game
        fields =["winnerId","get_winner","runnerup1","runnerup2","loser","is_ended","turn","players","n","lastTurn","dice","lastplayed"]

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields =["name","text"]

from rest_framework import serializers
from .models import Game,Coordinates,Player

class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields =["x","y","number","initial","reached"]


class PlayerSerializer(serializers.ModelSerializer):
    coordinates = CoordinateSerializer(many=True)
    class Meta:
        model = Player
        fields =["name","turn","color","colorId","complete","coordinates"]

class GameSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)
    class Meta:
        model = Game
        fields =["winnerId","get_winner","runnerup1","runnerup2","loser","is_ended","players"]
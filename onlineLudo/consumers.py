import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import OnlineGameToken,Message
from .serializers import GameSerializer,MessageSerializer
from ludo.views import get_index

class LudoConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.player_token = self.scope['url_route']['kwargs']['player']
        self.room_group_name = 'ludo_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        try:
            self.game = OnlineGameToken.objects.get(key=self.room_name).game
            self.player = self.game.players.get(token=self.player_token)
            self.player.active = True
            self.player.save()
            
            self.accept()
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'play',
                    "func":"update"
                }
            )
        except:
            self.player=False
            self.game = False
            pass
        


    def disconnect(self,closecode):
        if self.player and self.game:
            self.player.active = False
            self.player.save()
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'play',
                    "func":"update"
                }
            )
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self,text_data):
        maindata = json.loads(text_data)
        data = maindata
        if "message" in data and "name" in data:
            Message.objects.create(name = data["name"],text=data["message"],game=self.game)
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message'
                }
            )
        if "game" in maindata:
            data =maindata["game"]
            
            if "ended" in data and "loser" in data and "players" in data and "runnerup1" in data and "runnerup2" in data and "turn" in data and "winner" in data and "winnerId" in data:
                self.game.ended = data["ended"]
                self.game.loser = data["loser"]
                self.game.runnerup1 = data["runnerup1"]
                self.game.runnerup2 = data["runnerup2"]
                self.game.turn = data["turn"]
                self.game.winnerId = data["winnerId"]
                self.game.winner = data["winner"]
                self.game.lastTurn = self.player.colorId
                self.game.save()
                for player in self.game.players.all():
                    for c in player.coordinates.all():
                        coordinate = data["players"][get_index(data["players"],player.colorId)]["coordinates"][c.number]
                        c.x = coordinate["x"]
                        c.y = coordinate["y"]
                        c.initial= coordinate["initial"]
                        c.reached= coordinate["reached"]
                        c.save()
                
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'play',
                        "func":"play"
                    }
                )

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'play',
                    'func':"play"
                }
            )

    def chat_message(self, event):
        messages = list(MessageSerializer(self.game.msgs.all(),many=True).data)
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': messages
        })) 
    def play(self,event):
        data = GameSerializer(self.game).data
        data["player"] = self.player.colorId
        data["type"]=event["func"]
        self.send(text_data=json.dumps(data))
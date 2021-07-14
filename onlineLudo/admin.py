from django.contrib import admin
from . models import OnlineGame,OnlinePlayer,OnlineGameToken,Coord,Message,OldCoordinate
# Register your models here.

admin.site.register(OnlineGame)
admin.site.register(OnlinePlayer)
admin.site.register(OnlineGameToken)
admin.site.register(Coord)
admin.site.register(Message)
admin.site.register(OldCoordinate)

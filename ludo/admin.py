from django.contrib import admin
from .models import Game,Player,Coordinates,GameToken,ChatMessage

# Register your models here.
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Coordinates)
admin.site.register(GameToken)
admin.site.register(ChatMessage)

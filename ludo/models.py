from django.db import models
from .intial import initial_position,colors
from .path import Paths


# Create your models here.

class Game(models.Model):
    winnerId = models.IntegerField(null=True,blank=True)
    winner = models.CharField(default="",max_length=40)
    runnerup1 = models.CharField(default="",max_length=40)
    runnerup2 = models.CharField(default="",max_length=40)
    loser = models.CharField(default="",max_length=40)
    ended = models.BooleanField(default=False)
    No_of_players = models.IntegerField()
    dateTime = models.DateTimeField(auto_now_add=True)

    @property
    def get_winner(self):
        if self.winner:
            return self.winner
        for player in self.players.all():
            if player.complete:
                winner =""
                if player.name:
                    winner = player.name
                else:
                    winner = player.color
                self.winner = winner
                self.winnerId = player.colorId

                return winner
        return False

    @property
    def is_ended(self):
        if self.ended:
            return True
        for player in self.players.all():
            if player.complete:
                if not self.winner:
                    winner =""
                    if player.name:
                        winner = player.name
                    else:
                        winner = player.color
                    self.winner = winner
                    self.winnerId = player.colorId
                    self.save()
                
                elif not self.runnerup1:
                    p =""
                    if player.name:
                        p = player.name
                    else:
                        p = player.color
                    self.runnerup1 = p
                    self.save()

                elif not self.runnerup2:
                    p =""
                    if player.name:
                        p = player.name
                    else:
                        p = player.color
                    self.runnerup2 = p
                    self.save()

                else:
                    p =""
                    if player.name:
                        p = player.name
                    else:
                        p = player.color
                    self.loser = p
                    self.save()
            return False

        self.ended = True
        self.save()
        return True

                
                


    def get_initial_coordinates(self,color,player):
        positions = initial_position[color]
        i=0
        for p in positions:
            coo = Coordinates(y=p[0] , x =p[1],player=player,number=i)
            coo.save()
            i+=1
    

    def initialize(self,list_players,names=[]):
        self.save()
        players = []
        for i in list_players:
            player =Player(colorId=i,game=self,color=colors[i])
            players.append(player)

            if list_players[0]==i:
                player.turn = True
            else:
                player.turn = False
            player.save()
            self.get_initial_coordinates(i,player)
            if len(list(self.players.all())) >= 4:
                return True
        
        for i in range(len(names)):
            players[i].name = names[i]
            players[i].save()

    def __str__(self):
        return f"{self.id}. {self.No_of_players} players ,time : {self.dateTime}"

    def reinitialize(self):
        for p in list(self.players.all()):
            if p.colorId==0:
                p.turn = True
            else:
                p.turn = True
            for coordinate in list(p.coordinates.all()):
                coordinate.y= initial_position[p.colorId][coordinate.number][0]
                coordinate.x= initial_position[p.colorId][coordinate.number][1]
                coordinate.initial = True
                coordinate.save()
            p.save()


class Player(models.Model):
    name = models.CharField(max_length=50,default="")
    turn=models.BooleanField(default=False)
    color = models.CharField(max_length=30)
    colorId = models.IntegerField()
    game = models.ForeignKey(Game,on_delete=models.CASCADE,related_name="players")

    def __str__(self):
        if(self.name):
            return f"{self.name} : game {self.game.id}"
        return f"{self.color} : game {self.game.id}"

    @property
    def complete(self):
        for c in self.coordinates.all():
            if not c.reached:
                return False
        return True




class Coordinates(models.Model):
    y=models.IntegerField()
    x=models.IntegerField()
    number = models.IntegerField()
    initial = models.BooleanField(default=True)
    reached = models.BooleanField(default=False)
    player = models.ForeignKey(Player,on_delete=models.CASCADE,related_name="coordinates")

    def __str__(self):
        return f"{self.player.color}{self.number} : ({self.x}, {self.y}) "
    
    def initialize(self):
        self.y = initial_position[self.player.colorId][self.number][0]
        self.x = initial_position[self.player.colorId][self.number][1]
        self.save()

    def step(self,step):
        if step> 6 or step<1:
            return False
        if self.reached:
            return False
        if self.initial:
            if step ==6:
                self.y = Paths[self.player.colorId][0][0]
                self.x = Paths[self.player.colorId][0][1]
                self.initial = False
                self.save()
                return True
            return False

        current = [self.y,self.x]
        start = False
        step_up = 0
        for pos in Paths[self.player.colorId]:
            if start:
                step_up +=1
            if step_up ==step:
                self.y = pos[0]
                self.x = pos[1]
                if [self.y ,self.x] == Paths[self.player.colorId][56]:
                    self.reached = True
                self.save()
                return True
            if pos == current:
                start = True

        return False


class GameToken(models.Model):
    key = models.CharField(max_length=30)
    game = models.OneToOneField(Game, related_name="token",on_delete=models.CASCADE)

    def __str__(self):
        return self.key


    

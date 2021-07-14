from django.db import models
from store.views import get_random_string
# Create your models here.
from re import S
from django.db import models
from ludo.intial import initial_position,colors
from ludo.path import Paths,safe


# Create your models here.
class OldCoordinate(models.Model):
    x= models.IntegerField()
    y= models.IntegerField()

    def __str__(self):
        return f"({self.x},{self.y})"

class OnlineGame(models.Model):
    winnerId = models.IntegerField(null=True,blank=True)
    winner = models.CharField(default="",max_length=40)
    runnerup1 = models.CharField(default="",max_length=40)
    runnerup2 = models.CharField(default="",max_length=40)
    loser = models.CharField(default="",max_length=40)
    ended = models.BooleanField(default=False)
    turn = models.IntegerField(default=0)
    dateTime = models.DateTimeField(auto_now_add=True)
    lastTurn = models.IntegerField(default=-1)
    dice= models.IntegerField(default=0)
    old= models.OneToOneField(OldCoordinate,on_delete=models.CASCADE)

    def check_attack(self,c):
        for player in self.players.all():
            if not player.colorId ==c.player.colorId:
                for b in player.coordinates.all():
                    if b.x == c.x and b.y == c.y:
                        b.initialize()

    @property
    def n(self):
        return len(list(self.players.filter(active=True)))
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


    def initialize(self,colorId,name=""):
        self.turn = colorId
        self.save()
        player =OnlinePlayer(colorId=colorId)
        player.turn = True
        player.initialize(self,name=name)
        player.host = True
        player.save()
        return player.token

    def __str__(self):
        return f"{self.id}. {len(list(self.players.all()))} players ,time : {self.dateTime}"

    def reinitialize(self):
        self.turn = 0
        self.save()
        for p in list(self.players.all()):
            if p.colorId==0:
                p.turn = True
            else:
                p.turn = True
            for coordinate in list(p.coordinates.all()):
                coordinate.y= initial_position[p.colorId][coordinate.number][0]
                coordinate.x= initial_position[p.colorId][coordinate.number][1]
                coordinate.initial = True
                coordinate.reached = False
                coordinate.save()
            p.save()


    def nextTurn(self,colorId):
        if colorId >= 3 :
            return 0;
        else:
            return colorId + 1;
    def nextPlayer(self,colorId,playerlists):
        if self.nextTurn(colorId) in playerlists:
            return self.nextTurn(colorId)
        return self.nextPlayer(self.nextTurn(colorId),playerlists)
    def get_next_turn(self):
        l = []
        for player in self.players.all():
            player.turn = False
            player.save()
            if not player.complete:
                l.append(player.colorId)

        nextplayer = self.nextPlayer(self.turn,l)
        Np = self.players.get(colorId=nextplayer)
        Np.turn = True
        Np.save()
        self.turn = nextplayer
        self.save()


class Step(models.Model):
    x= models.IntegerField()
    y= models.IntegerField()
    game=models.ForeignKey(OnlineGame,on_delete=models.CASCADE,related_name="steps")



class OnlinePlayer(models.Model):
    name = models.CharField(max_length=50,default="")
    turn=models.BooleanField(default=False)
    color = models.CharField(max_length=30,default="")
    colorId = models.IntegerField()
    token = models.CharField(max_length=30,default="")
    game = models.ForeignKey(OnlineGame,on_delete=models.CASCADE,related_name="players")
    active = models.BooleanField(default=False)
    host = models.BooleanField(default=False)
    updateGame = models.BooleanField(default=False)
    updateMessage = models.BooleanField(default=False)
    refresh = models.BooleanField(default=False)
    


    def initialize(self,game,name=""):
        self.name = name
        self.color = colors[self.colorId]
        self.token = get_random_string(10)
        self.game = game
        self.save()
        for i in range(4):
            c = Coord(number=i,player=self)
            c.initialize()
            c.save()

        

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
    @property
    def onground(self):
        for c in self.coordinates.all():
            if not c.initial and not c.reached :
                return True
        return False

    def update_turn(self,stepped):
        if not stepped:
            for c in self.coordinates.all():
                if not c.initial and not c.reached:
                    return False
        self.game.get_next_turn()
        return True
    @property
    def singleturn(self):
        data = []
        for c in self.coordinates.all():
            if not c.initial and not c.reached :
                data.append(c.number)
        if len(data)==1:
            return {"value":True,"number":data[0]}
        return {"value":False}
        

class Coord(models.Model):
    y=models.IntegerField(default=0)
    x=models.IntegerField(default=0)
    number = models.IntegerField()
    initial = models.BooleanField(default=True)
    reached = models.BooleanField(default=False)
    player = models.ForeignKey(OnlinePlayer,on_delete=models.CASCADE,related_name="coordinates")

    def __str__(self):
        return f"{self.player.color}{self.number} : ({self.x}, {self.y}) "
    
    def initialize(self):
        self.y = initial_position[self.player.colorId][self.number][0]
        self.x = initial_position[self.player.colorId][self.number][1]
        self.initial = True
        self.save()

    def step(self,step):
        if step> 6 or step<1:
            return False,[]
        if self.reached:
            return False,[]
        if self.initial:
            if step ==6:
                self.y = Paths[self.player.colorId][0][0]
                self.x = Paths[self.player.colorId][0][1]
                self.initial = False
                self.save()
                return True,[]
            return False , []

        current = [self.y,self.x]
        start = False
        step_up = 0
        steps = []
        for pos in Paths[self.player.colorId]:
            if start:
                step_up +=1 
                steps.append(pos)
            if step_up ==step:
                self.y = pos[0]
                self.x = pos[1]
                if [self.y ,self.x] == Paths[self.player.colorId][56]:
                    self.reached = True
                self.save()

                if not self.safe():
                    self.player.game.check_attack(self)
                return True ,steps
            if pos == current:
                start = True
        
        return False,steps

    def safe(self):
        return [self.y, self.x] in safe or [self.y, self.x] in initial_position[self.player.colorId]


class OnlineGameToken(models.Model):
    key = models.CharField(max_length=30)
    game = models.OneToOneField(OnlineGame, related_name="token",on_delete=models.CASCADE)

    def __str__(self):
        return self.key


class Message(models.Model):
    name = models.CharField(max_length=50,default="log")
    text = models.CharField(max_length=300)
    game = models.ForeignKey(OnlineGame,on_delete=models.CASCADE,related_name="msgs")
    

    

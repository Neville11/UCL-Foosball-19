##########################
# Code designs the objects which Soccer Players and Balls, are to be represented as
# And generates their instances for use in Screens.py
# It also designs the features of the team Management system 
#and  their implications on player ability 
########################

########################
#MatchSetup.py
#Entire code:Original Code
########################
import math
import pygame
import random
from player_Design import*

class playerRepH(object):
    def __init__(self,team,player,x,y,wearH,r=15):
        self.x,self.y,self.r=x,y,r
        self.matchPlayer=player
        self.playerTeam=team
        self.fontType=pygame.font.SysFont("Comic Sans MS",self.r)
        self.kit=wearH
        if isinstance(player,Defender):
            self.pace=team.defPace
        elif isinstance(player,Midfielder):
            self.pace=team.midPace
        elif isinstance(player,Forward):
            self.pace=team.forPace
        else:
            self.pace=self.matchPlayer.reaction
        
            
    def draw(self,screen):
        pygame.draw.circle(screen,self.kit[0],(int(self.x),int(self.y)),self.r)
        playerNum=self.fontType.render(str(self.matchPlayer.num),False,self.kit[1])
        playerNum=pygame.transform.rotate(playerNum,-90)
        if self.matchPlayer.num>=10:
            screen.blit(playerNum,(self.x-self.r,self.y-self.r//2))
        else:
            screen.blit(playerNum,(self.x-self.r,self.y-self.r//4))
    def shoot(self,ball):
        rSelf=math.sqrt(((ball.x-self.x)**2 +(self.y-ball.y)**2))
        if rSelf<=self.r+ball.r:
            bX=ball.x+ball.r*math.cos(math.radians(ball.angle))
            theta=(bX-self.x)/ball.r
            if theta>=0:
                ball.vel=self.matchPlayer.attack/5
                ball.angle=(ball.angle+180)%360

class playerRepA(object):
    def __init__(self,team,player,x,y,wearA,r=15):
        pygame.sprite.Sprite.__init__(self)
        self.x,self.y,self.r=x,y,r
        self.matchPlayer=player
        self.playerTeam=team
        self.kit=wearA
        self.fontType=pygame.font.SysFont("Comic Sans MS",self.r)
        if isinstance(player,Defender):
            self.pace=team.defPace
        elif isinstance(player,Midfielder):
            self.pace=team.midPace
        elif isinstance(player,Forward):
            self.pace=team.forPace
        else:
            self.pace=self.matchPlayer.reaction
    
    def draw(self,screen):
        pygame.draw.circle(screen,self.kit[0],(int(self.x),int(self.y)),self.r)
        playerNum=self.fontType.render(str(self.matchPlayer.num),False,self.kit[1])
        playerNum=pygame.transform.rotate(playerNum,90)
        if self.matchPlayer.num>=10:
            screen.blit(playerNum,(self.x-self.r,self.y-self.r//2))
        else:
            screen.blit(playerNum,(self.x-self.r,self.y-self.r//4))
    
    def shoot(self,ball):
        rSelf=math.sqrt(((ball.x-self.x)**2 +(ball.y-self.y)**2))
        if rSelf<=self.r+ball.r:
            bX=ball.x+ball.r*math.cos(math.radians(ball.angle))
            theta=(bX-self.x)/ball.r
            if theta<=0:
                ball.vel+=self.matchPlayer.attack/5
                ball.angle=(ball.angle+180)%360
                    
def createReps(home,away):
    homePlayers,awayPlayers=[],[]
    x,y,dx,yStart,yEnd,maxRow=200,220,100,50,385,6
    wearH,wearA=None,None
    for numH,kitH in enumerate(home.kitColors):
        if not(wearH and wearA):
            for numA,kitA  in enumerate(away.kitColors):
                if kitH!=kitA:
                    wearH=[kitH,home.kitColors[(numH+1)%len(home.kitColors)]]
                    wearA=[kitA,away.kitColors[(numA+1)%len(away.kitColors)]]
                    break
                elif 2==numH==numA:
                    wearH=[home.kitColors[0],home.kitColors[(numH+1)%len(home.kitColors)]]
                    wearA=[away.kitColors[1],away.kitColors[(numA+1)%len(away.kitColors)]]

    for pos in range(len(home.players)):
        numP=len(home.players[pos])
        dy=(yEnd-yStart)/(maxRow-1)
        if pos!=0:
            y=yStart+(0.5*(maxRow-numP)*dy)
        if pos==1:
            dx+=50
        elif pos==2:
            dx+=20
        homePlayers.append(list())
        for player in home.players[pos]:
            if pos==0:
                homePlayers[pos].append(playerRepH(home,player,x,y,wearH,8))
            else:
                homePlayers[pos].append(playerRepH(home,player,x,y,wearH))
            y+=dy
        x+=dx
    
    x,y,dx,yStart,yEnd,maxRow=760,220,-100,50,385,6
    for pos in range(len(away.players)):
        numP=len(away.players[pos])
        dy=(yEnd-yStart)/(maxRow-1)
        if pos!=0:
            y=yStart+(0.5*(maxRow-numP)*dy)
        if pos==1:
            dx-=50
        elif pos==2:
            dx-=20
        awayPlayers.append(list())
        for player in away.players[pos]:
            if pos==0:
                awayPlayers[pos].append(playerRepA(away,player,x,y,wearA,8))
            else:
                awayPlayers[pos].append(playerRepA(away,player,x,y,wearA))
            y+=dy
        x+=dx
    xstart,ystart,vel,angle=488,225,4,random.choice([0,180])
    ball=Ball("ball.png",vel,angle,xstart,ystart)
    return [homePlayers,awayPlayers,ball]

class Ball(object):
    def __init__(self,rep,vel,angle,x,y,r=6):
        self.img=pygame.image.load(rep)
        self.img=pygame.transform.scale(self.img,(2*r,2*r))
        self.img.set_colorkey((255,255,255))
        self.vel=vel
        self.angle=angle
        self.x,self.y,self.r=x,y,r
        self.ballTrack={}
        self.deadBall=False
    
    def update(self):
        self.x+=self.vel*math.cos(math.radians(self.angle))
        self.y+=self.vel*math.sin(math.radians(self.angle))
        
    def checkWall(self,xUp,xDown,yUp,yDown,y1,y2):
        if not((self.x+self.r<=xUp+5 and y1+2*self.r<=self.y+self.r<=y2) or \
        (self.x-self.r>=xDown-5 and y1+2*self.r<=self.y+self.r<= y2)):
            if self.x+self.vel*math.cos(math.radians(self.angle))>=xDown:
                self.angle=(self.angle+(180-2*(self.angle%90)))%360
                self.x=760
            elif self.x+self.vel*math.cos(math.radians(self.angle))<=xUp:
                self.angle=(self.angle+(180-2*(self.angle%90)))%360
                self.x=202
            elif self.y+self.vel*math.sin(math.radians(self.angle))>=yDown:
                self.angle=(self.angle+(180-2*(self.angle%90)))%360
                self.y=404 
            elif self.y+self.vel*math.sin(math.radians(self.angle))<=yUp:
                self.angle=(self.angle+(180-2*(self.angle%90)))%360
                self.y=36 
        else:
            print(xUp,self.x,xDown,y1,self.y,y2)
    
    def isGoal(self,p1X1,p2X1,y1,y2,homeSc,awaySc,paused):
        x=self.x+self.vel*math.cos(math.radians(self.angle))
        y=self.y+self.vel*math.sin(math.radians(self.angle))
        if (x+self.r<=p1X1 and y1+self.r<=y+self.r<=y2):
            x0,y0,oVel,ang0=488,225,3,random.choice([0,180])
            self.x,self.vel,self.y,self.angle=x0,oVel,y0,ang0
            paused=True
            return(homeSc,awaySc+1,paused)
        elif (x-self.r>=p2X1 and y1+self.r<=y+self.r<= y2):
            x0,y0,oVel,ang0=488,225,3,random.choice([0,180])
            self.x,self.vel,self.y,self.angle=x0,oVel,y0,ang0
            paused=True
            return(homeSc+1,awaySc,paused)
        return (homeSc,awaySc,paused)
            
        
    
    def checkCollision(self,player):
        rSelf=math.sqrt(((self.x-player.x)**2 +(self.y-player.y)**2))
        if rSelf<=self.r+player.r:
            rSelf//=2
            theta=math.degrees(math.acos((rSelf-self.r)/self.r)) 
            direction=random.choice([-1,1])
            maxT,maxOff=20,45
            if not isinstance(player.matchPlayer,Goalie):
                offset=direction*(player.matchPlayer.technique/maxT)*maxOff
                self.angle=((self.angle-180)+offset)%360
                dVel=(maxT-player.matchPlayer.defence)/10
                self.vel+=dVel
            else:
                offset=direction*((maxT-player.matchPlayer.reaction)/maxT)*maxOff
                self.angle=((self.angle-180)+offset)%360
  
    def gravity(self):
        if self.vel>=3:
            self.vel-=0.25
    
    def isDeadBall(self):
        if len(self.ballTrack)>=10 and len(self.ballTrack)%2==0:
            check=list(self.ballTrack)[-10:]
            angles=[]
            for i in check:
                angles.append(self.ballTrack[i])
            angles.sort()
            if len(set(angles))<=2:
                self.deadBall=True
                self.ballTrack.clear()
            else:
                self.deadBall=False

class Formations(object):
    def __init__(self,formation):
        self.formation=formation
        self.selected=False
        self.onMe=False    
    
    def __repr__(self):
        app=str(self.formation)[1:-1]
        app=app.replace(",","--")
        app=app.replace(" ","")
        return app 
    
    def draw(self,screen,x,y,w=91,h=25,bord=2):
        YELLOW=(167,184,211)
        self.outer=[x,y,w,h]
        self.inner=pygame.Rect(self.outer).inflate(-bord*2,-bord*2)
        self.fontType=pygame.font.SysFont("Comic Sans MS",14)
        disp=self.fontType.render(self.__repr__(),False,(255,255,255))
        pygame.draw.rect(screen,(0,0,0),self.outer)
        if self.onMe:
            pygame.draw.rect(screen,YELLOW,self.inner)
        else:
            pygame.draw.rect(screen,(0,0,0),self.inner)
        screen.blit(disp,self.inner[:2])
    
    def drawPlayers(self,screen,home,x1,y1,x2,y2):
        x,y,dx,yStart,yEnd,maxRow=x1,y1,x2,y2,10,6
        if self.selected:
            home.formation=self.formation
            wearH=[home.kitColors[1]]
            self.seenP=[]
            for pos in range(len(self.formation)):
                numP=self.formation[pos]
                dy=(yEnd-yStart)/(maxRow-1)
                if pos!=0:
                    y=yStart+(0.5*(maxRow-numP)*dy)
                if pos==1:
                    dx+=50
                elif pos==2:
                    dx+=20
                self.seenP.append(list())
                for player in range(self.formation[pos]):
                    if pos==0:
                        self.seenP.append(playerRepH(home[pos][player],x,y,wearH,4))
                    else:
                        self.seenP.append(playerRepH(home,player,x,y,wearH,6))
                    y+=dy
                x+=dx
            for pos in self.seenP:
                for player in pos:
                    player.draw()
            
class TFT(Formations):
    def __init__(self,formation=[3,4,3]):
        super().__init__(formation)

class TFiTw(Formations):
    def __init__(self,formation=[3,5,2]):
        super().__init__(formation)
        
class TSO(Formations):
    def __init__(self,formation=[3,6,1]):
        super().__init__(formation)
        
class FTT(Formations):
    def __init__(self,formation=[4,3,3]):
        super().__init__(formation)
        
class FFTw(Formations):
    def __init__(self,formation=[4,4,2]):
        super().__init__(formation)
        
class FFiO(Formations):
    def __init__(self,formation=[4,5,1]):
        super().__init__(formation)

class FFiO(Formations):
    def __init__(self,formation=[4,5,1]):
        super().__init__(formation)

class FTwF(Formations):
    def __init__(self,formation=[4,2,4]):
        super().__init__(formation)
        
class FiFO(Formations):
    def __init__(self,formation=[5,4,1]):
        super().__init__(formation)
        
class FiTwT(Formations):
    def __init__(self,formation=[5,2,3]):
        super().__init__(formation)

class FiTTw(Formations):
    def __init__(self,formation=[5,3,2]):
        super().__init__(formation)
    
class Strategies(object):
    def __init__(self,name):
        self.name=name
        self.selected,self.onMe=False,False
    def __repr__(self):
        return self.name
    
    def draw(self,screen,x,y,w=91,h=25,bord=2):
        YELLOW=(167,184,211)
        self.outer=[x,y,w,h]
        self.inner=pygame.Rect(self.outer).inflate(-bord*2,-bord*2)
        self.fontType=pygame.font.SysFont("Comic Sans MS",14)
        disp=self.fontType.render(self.__repr__(),False,(255,255,255))
        pygame.draw.rect(screen,(0,0,0),self.outer)
        if self.onMe:
            pygame.draw.rect(screen,YELLOW,self.inner)
        else:
            pygame.draw.rect(screen,(0,0,0),self.inner)
        screen.blit(disp,self.inner[:2])
        
    def info(self):
        pass
class Counter(Strategies):
    def __init__(self,name="Counter"):
        super().__init__(name)

class HighPress(Strategies):
    def __init__(self, name="High Press"):
        super().__init__(name)

class TikiTaka(Strategies):
    def __init__(self, name="Tiki Taka"):
        super().__init__(name)
class Defensive(Strategies):
    def __init__(self, name="Defensive"):
        super().__init__(name)

class Attack(Strategies):
    def __init__(self, name="Attack"):
        super().__init__(name)

class WingPlay(Strategies):
    def __init__(self, name="Wing Play"):
        super().__init__(name)

def getFormAndStrat():
    return [
            [TFT(),
            TSO(),
            FTT(),
            FFTw(),
            FTwF(),
            FFiO(),
            FiFO(),
            FiTwT(),
            FiTTw(),
                                ],
            [TFT(),
            TSO(),
            FTT(),
            FFTw(),
            FTwF(),
            FFiO(),
            FiFO(),
            FiTwT(),
            FiTTw(),
                                ],
            [Counter(),
            HighPress(),
            TikiTaka(),
            Defensive(),
            Attack(),
            WingPlay()          ],
            [Counter(),
            HighPress(),
            TikiTaka(),
            Defensive(),
            Attack(),
            WingPlay()          ],
    ]
 

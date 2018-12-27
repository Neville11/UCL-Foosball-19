##########################
# Code designs the Object Oriented Structure for soccer teams and players
########################

########################
#player_Design.py
#Entire code:Original Code
########################
import pygame 

class Player(object):
    def __init__(self,name,num,attributes,team):
        self.attack,self.defence,self.pace,self.technique,self.aggression=attributes
        self.name=name
        self.num=num
        self.goals=0
        self.team=team
        self.selected,self.onMe=False,False
        self.fontType=pygame.font.SysFont("Comic Sans MS",12)
        self.font2=pygame.font.SysFont("Times New Roman",10)
    def scoreGoal(self):
        self.goals+=1
    
    def drawBox(self,screen,x,y,w=194,h=19):
        YELLOW=(167,184,211)
        bord=2
        self.outBox=[x,y,w,h]
        self.innBox=pygame.Rect(self.outBox).inflate(-bord*2,-bord*2)
        pygame.draw.rect(screen,(0,0,0),self.outBox)
        if self.onMe:
            pygame.draw.rect(screen,(255,255,255),self.innBox)
        else:
            pygame.draw.rect(screen,YELLOW,self.innBox)
        disp=self.fontType.render(self.name,False,(0,0,0))
        screen.blit(disp,self.innBox[:2])
    
    def drawAtt(self,screen,outBox):
        colors=[(226, 57, 31),(211, 161, 35),(209, 194, 64),(54, 130, 54),(1,128,1)]
        barC=(97, 80, 109)
        marg,numAtt=5,5
        area=pygame.Rect(outBox).inflate(-marg*2,-marg)
        startX,startY,bord=area[0],area[1],2
        for i in range(numAtt):
            w,h1,h2,dw,dy=18,20,130,5,10
            if i==0:
                stat1=self.font2.render("ATT",False,(255,255,255))
                box1=[startX,startY,w,h1]
                fullB1=[startX,startY+h1+dy,w,h2]
                pH1=fullB1[3]*self.attack/20
                attCode=self.attack//5
                pBar1=[startX+bord,startY+h1+dy,w-bord,pH1]
                screen.blit(stat1,box1[:2])
                pygame.draw.rect(screen,barC,fullB1,bord)
                pygame.draw.rect(screen,colors[attCode],pBar1)
                startX+=w+dw
            elif i==1:
                stat2=self.font2.render("DEF",False,(255,255,255))
                box2=[startX,startY,w,h1]
                fullB2=[startX,startY+h1+dy,w,h2]
                pH2=fullB1[3]*self.defence/20
                defCode=self.defence//5
                pBar2=[startX+bord,startY+h1+dy,w-bord,pH2]
                screen.blit(stat2,box2[:2])
                pygame.draw.rect(screen,barC,fullB2,bord)
                pygame.draw.rect(screen,colors[defCode],pBar2)
                startX+=w+dw
            elif i==2:
                stat3=self.font2.render("PAC",False,(255,255,255))
                box3=[startX,startY,w,h1]
                fullB3=[startX,startY+h1+dy,w,h2]
                pH3=fullB3[3]*self.pace/20
                pacCode=self.pace//5
                pBar3=[startX+bord,startY+h1+dy,w-bord,pH3]
                screen.blit(stat3,box3[:2])
                pygame.draw.rect(screen,barC,fullB3,bord)
                pygame.draw.rect(screen,colors[pacCode],pBar3)
                startX+=w+dw
            elif i==3:
                stat4=self.font2.render("TEC",False,(255,255,255))
                box4=[startX,startY,w,h1]
                fullB4=[startX,startY+h1+dy,w,h2]
                pH4=fullB4[3]*self.technique/20
                tecCode=self.technique//5
                pBar4=[startX+bord,startY+h1+dy,w-bord,pH4]
                screen.blit(stat4,box4[:2])
                pygame.draw.rect(screen,barC,fullB4,bord)
                pygame.draw.rect(screen,colors[tecCode],pBar4)
                startX+=w+dw
            else:
                stat5=self.font2.render("AGG",False,(255,255,255))
                box5=[startX,startY,w,h1]
                fullB5=[startX,startY+h1+dy,w,h2]
                pH5=fullB5[3]*self.aggression/20
                aggCode=self.aggression//5
                pBar5=[startX+bord,startY+h1+dy,w-bord,pH5]
                screen.blit(stat5,box5[:2])
                pygame.draw.rect(screen,barC,fullB5,bord)
                pygame.draw.rect(screen,colors[aggCode],pBar5)
    
class Goalie(Player):
    def __init__(self,name,num,attributes,team):
        self.name=name
        self.num=num
        self.team=team
        self.reaction,self.technique=attributes
        self.cleanS=0
        self.team=team
        self.selected,self.onMe=False,False
        self.fontType=pygame.font.SysFont("Comic Sans MS",12)
        self.font2=pygame.font.SysFont("Times New Roman",10)
    
    def keepsCleanSheet(self):
        self.cleanS+=1
    
    def drawAtt(self,screen,outBox):
        colors=[(226, 57, 31),(211, 161, 35),(209, 194, 64),(54, 130, 54),(1,128,1)]
        barC=(97, 80, 109)
        marg,numAtt=5,5
        area=pygame.Rect(outBox).inflate(-marg*2,-marg)
        startX,startY,bord=area[0],area[1],2
        for i in range(numAtt):
            w,h1,h2,dw,dy=40,20,130,25,10
            if i==0:
                stat1=self.font2.render("REAC",False,(255,255,255))
                box1=[startX,startY,w,h1]
                fullB1=[startX,startY+h1+dy,w,h2]
                pH1=fullB1[3]*self.reaction/20
                reacCode=self.reaction//5
                pBar1=[startX+bord,startY+h1+dy,w-bord,pH1]
                screen.blit(stat1,box1[:2])
                pygame.draw.rect(screen,barC,fullB1,bord)
                pygame.draw.rect(screen,colors[reacCode],pBar1)
                startX+=w+dw
            elif i==1:
                stat2=self.font2.render("TEC",False,(255,255,255))
                box2=[startX,startY,w,h1]
                fullB2=[startX,startY+h1+dy,w,h2]
                pH2=fullB1[3]*self.technique/20
                defCode=self.technique//5
                pBar2=[startX+bord,startY+h1+dy,w-bord,pH2]
                screen.blit(stat2,box2[:2])
                pygame.draw.rect(screen,barC,fullB2,bord)
                pygame.draw.rect(screen,colors[defCode],pBar2)
                
class Midfielder(Player):
    pass
class Forward(Player):
    pass
    
class Defender(Player):
    pass
    
class Team(object):
    def __init__(self,name,kitColors,abbv,formation,logo):
        self.name=name
        self.kitColors=kitColors
        self.abbv=abbv
        self.players=None
        self.formation=formation
        self.attack,self.defence,self.aggression,self.pace,self.technique=0,0,0,0,0
        self.logo=logo
    

    def getTeamAvg(self):
        numPlayers=11
        self.defPace,self.midPace,self.forPace=0,0,0
        for pos in self.players:
            for player in pos:
                if isinstance(player,Defender):
                    self.defPace+= player.pace/len(pos)
                elif isinstance(player,Midfielder):
                    self.midPace+= player.pace/len(pos)
                elif isinstance(player,Forward):
                    self.forPace+= player.pace/len(pos)
                if not (isinstance(player,Goalie)):
                    self.aggression+=player.aggression/numPlayers
                    self.pace+=player.pace/numPlayers
                    self.technique+=player.technique/numPlayers
                    
                    if not (isinstance(player,Midfielder) and isinstance(player,Defender)):
                        self.defence+=(player.defence+player.technique)/(2*(len(self.players[2])+len(self.players[3])))
                    elif not (isinstance(player,Midfielder) and isinstance(player,Forward)):
                        self.attack+=(player.attack+player.pace)/(2*(len(self.players[2])+len(self.players[3])))
        self.ovr=(self.attack+self.defence+self.aggression+self.pace+self.technique)/5
    

    
     
        
        
 
    
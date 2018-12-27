##########################
# Code designs Object Oriented Structure for movement between Game screens as well as runs Game 
########################

#######################
#Lines 21-96: Code taken from 112 pygame template by Lukas Peraza
#Lines 100-End:Original Code
#Various Lines: Backgroud images from google images(various sources)
#Line 906: Video gotten from https://www.youtube.com/watch?v=jNGoz9Zze6c
#######################

import module_manager
import pygame
from generatePlayers import*
from MatchSetup import*
import random
import moviepy
from moviepy.editor import *

teams=generateGame()
details=getFormAndStrat()

class Screen(object):

    def init(self):
        pass

    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass
    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        pass
    def isKeyPressed(self, key):
        return self._keys.get(key, False)

    def __init__(self, width=800, height=600, fps=50, title="Screen"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bg=pygame.image.load("UEFA Logo 1.jpg")
        self.bg=pygame.transform.scale(self.bg,(self.width,self.height))
        pygame.init()
        pygame.font.init()
        self.fontType=pygame.font.SysFont("Comic Sans MS",22)
        
    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height),0,32)
        pygame.display.set_caption(self.title)
        self._keys = dict()
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            self.redrawAll(screen)
            pygame.display.flip()
            screen.blit(self.bg,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            
        pygame.quit()


class Start(Screen):
    def __init__(self, width=1050, height=600, fps=10,title="Start"):
        super().__init__(width,height,fps,title)
        self.goodBall=(75,75)
        self.fontType=pygame.font.SysFont("Algerian",32)
        self.ball=pygame.image.load("BulletPoint.png")
        self.ball=pygame.transform.scale(self.ball,self.goodBall)
        self.ball.set_colorkey((255,255,255))
        self.img=pygame.image.load("hil.jpg")
        self.img=pygame.transform.scale(self.img,(380,55))
        self.img2=pygame.image.load("hil2.jpg")
        self.img2=pygame.transform.scale(self.img2,(380,55))
        self.eSel,self.ngSel,self.lgSel=False,False,False
        
    def redrawAll(self,screen):
        def Options(screen):
            numOptions,offset,dy,start=3,0,90,200
            goodBall,bord=(75,75),20
            BLACK=(0,0,0)
            for i in range(numOptions):
                xstart,ystart,bS=self.width//2-325,self.height//2-100+offset,100
                deltaX,deltaY=400,75
                if i==0:
                    self.exhibition=[xstart+bS ,ystart,deltaX,deltaY]
                    self.innerE=pygame.Rect(self.exhibition).inflate(-bord,-bord)
                    pygame.draw.rect(screen,BLACK,self.exhibition)
                    exhibitionF=self.fontType.render("TWO PLAYER MODE",False,(255,255,255))
                    screen.blit(self.ball,(xstart,ystart))
                    if self.eSel:
                        screen.blit(self.img2,(self.innerE[:2]))
                    else:
                        screen.blit(self.img,(self.innerE[:2]))
                    screen.blit(exhibitionF,(self.innerE[0]+30,self.innerE[1]))
                elif i==1:
                    self.newGame=[xstart+bS,ystart,deltaX,deltaY]
                    self.innerNG=pygame.Rect(self.newGame).inflate(-bord,-bord)
                    pygame.draw.rect(screen,BLACK,self.newGame)
                    newGameF=self.fontType.render("BEAT THE TACTICIAN",False,(255,255,255))
                    screen.blit(self.ball,(xstart,ystart))
                    if self.ngSel:
                        screen.blit(self.img2,(self.innerNG[:2]))
                        screen.blit(self.ball,(xstart,ystart))
                    else:
                        screen.blit(self.img,(self.innerNG[:2]))
                    screen.blit(newGameF,(self.innerNG[0]+20,self.innerNG[1]))
                    
                else:
                    self.loadGame=[xstart+bS,ystart,deltaX,deltaY]
                    self.innerLG=pygame.Rect(self.loadGame).inflate(-bord,-bord)
                    pygame.draw.rect(screen,BLACK,self.loadGame)
                    loadGameF=self.fontType.render("THE BETTER TACTICIAN?",False,(255,255,255))
                    screen.blit(self.ball,(xstart,ystart))
                    if self.lgSel:
                        screen.blit(self.img2,(self.innerLG[:2]))
                    else:
                        screen.blit(self.img,(self.innerLG[:2]))
                    screen.blit(loadGameF,(self.innerLG[0],self.innerLG[1]))
                
                offset+=dy
        Options(screen)
        
    def mouseMotion(self,x,y):
        if pygame.Rect((self.newGame)).collidepoint((x,y)):
            self.ngSel,self.lgSel,self.eSel=True,False,False
        elif pygame.Rect((self.loadGame)).collidepoint((x,y)):
            self.lgSel,self.ngSel,self.eSel=True,False,False
        elif pygame.Rect((self.exhibition)).collidepoint((x,y)):
            self.eSel,self.lgSel,self.ngSel=True,False,False
        else:
            self.eSel,self.lgSel,self.ngSel=False,False,False
    def mousePressed(self,x,y):
        if pygame.Rect((self.newGame)).collidepoint((x,y)):
            pass
        elif pygame.Rect((self.loadGame)).collidepoint((x,y)):
            pass
        elif pygame.Rect((self.exhibition)).collidepoint((x,y)):
            exhibitionSc=Exhibition()
            exhibitionSc.run()
        
class NewSave(Screen):
    def __init__(self, width=800, height=600, fps=10, title="New Save"):
        super().__init__(width,height,fps,title)
        self.bg=pygame.image.load("SaveScreen Logo.jpg")
        self.bg=pygame.transform.scale(self.bg,(self.width,self.height))
        
    def redrawAll(self,screen):
        def back(screen):
            margin,self.bSize=20,65
            YELLOW=(255,255,0)
            self.backB=[self.width-self.bSize-margin,margin,self.bSize,self.bSize]
            pygame.draw.rect(screen,YELLOW,self.backB,3)
            backF=self.fontType.render("BACK",False,(255,255,255))
            screen.blit(backF,(self.backB[0],self.backB[1]))
        
        screen.blit(self.bg,(0,0))
        back(screen)
    
    def mousePressed(self,x,y):
        if self.backB[0]<=x<=self.backB[0]+self.bSize and self.backB[1]<=y<=self.backB[1]+self.bSize:
            startSc=Start()
            startSc.run()
    
class showSaves(Screen):
    def __init__(self, width=800, height=600, fps=50, title="Saves"):
        super().__init__(width,height,fps,title)
        self.bg=pygame.image.load("SaveScreen Logo.jpg")
        self.bg=pygame.transform.scale(self.bg,(self.width,self.height))
    
    def redrawAll(self,screen):
        def saveSlots(screen):
            numSlots=3
            dx=50
            x,y,size=300,250,100
            YELLOW=(255,255,0)
            for i in range(numSlots):
                if i==0:
                    self.slot1=[x,y,size,size]
                    pygame.draw.rect(screen,YELLOW,self.slot1,3)
                    slot1F=self.fontType.render("SAVE 1",False,(255,255,255))
                    screen.blit(slot1F,(self.slot1[0],self.slot1[1]))
                elif i==1:
                    self.slot2=[x,y,size,size]
                    pygame.draw.rect(screen,YELLOW,self.slot2,3)
                    slot2F=self.fontType.render("SAVE 2",False,(255,255,255))
                    screen.blit(slot2F,(self.slot2[0],self.slot2[1]))
                else:
                    self.slot3=[x,y,size,size]
                    pygame.draw.rect(screen,YELLOW,self.slot3,3)
                    slot3F=self.fontType.render("SAVE 3",False,(255,255,255))
                    screen.blit(slot2F,(self.slot3[0],self.slot3[1]))
                x+=dx+size
                
        def back(screen):
            margin,self.bSize=20,65
            YELLOW=(255,255,0)
            self.backB=[self.width-self.bSize-margin,margin,self.bSize,self.bSize]
            pygame.draw.rect(screen,YELLOW,self.backB,5)
            backF=self.fontType.render("BACK",False,(255,255,255))
            screen.blit(backF,(self.backB[0],self.backB[1]))
        
        screen.blit(self.bg,(0,0))
        back(screen)
        saveSlots(screen)
        
    
    def mousePressed(self,x,y):
        savesB=[self.slot1,self.slot2,self.slot3]
        if self.backB[0]<=x<=self.backB[0]+self.bSize and self.backB[1]<=y<=self.backB[1]+self.bSize:
            startSc=Start()
            startSc.run()
        sSize=100
        for i in savesB:
            if i[0]<=x<=i[0]+sSize and i[1]<=y<=i[1]+sSize:
                homeSc=Home()
                homeSc.run()

    def mousePressed(self,x,y):
        if pygame.Rect((self.backB)).collidepoint((x,y)):
            homeSc=Home()
            homeSc.run()
        elif pygame.Rect((self.squadB)).collidepoint((x,y)):
            squadSc=Squad()
            squadSc.run()
        elif pygame.Rect((self.statsB)).collidepoint((x,y)):
            statsSc=Statistics()
            statsSc.run()
        elif pygame.Rect((self.tacticsB)).collidepoint((x,y)):
            tacticsSc=Tactics()
            tacticsSc.run()
    
class Matchday(Screen):
    pass
    
class MatchGame(Screen):
    def __init__(self,home,away,width=800, height=600, fps=100 , title="Match"):
        super().__init__(width,height,fps,title)
        self.bg=pygame.image.load("Matchbg.jpg")
        self.bg=pygame.transform.scale(self.bg,(self.width,self.height))
        self.home,self.away=home,away
        self.homeR,self.awayR,self.ball=createReps(home,away)
        self.homeSel,self.awaySel=2,2
        self.paused=True
        self.homeSc,self.awaySc=0,0
        self.ballT=0
        self.matchT="90"
        self.gameOver=False
        self.playL=pygame.image.load("pause.png")
        self.pauseL=pygame.image.load("play.png")
        self.exitL=pygame.image.load("exit.jpg")
        self.pitch=pygame.image.load("football-field.jpg")
        self.img1=pygame.image.load("hil3.jpg")
        self.img1=pygame.transform.scale(self.img1,(238,48))
        self.powerB=pygame.image.load("powerB.jpg")
        self.showCurrH,self.showCurrA={1:300,2:450,3:620},{1:658,2:510,3:340}
        self.font=pygame.font.SysFont("Haettenschweiler",50)
        self.font2=pygame.font.SysFont("Haettenschweiler",100)
    
    def keyPressed(self, keyCode, modifier):
        if not self.paused:
            homeL,homeR,awayL,awayR=ord("a"),ord("d"),276,275
            if keyCode==homeL and self.homeSel>0:
                self.homeSel-=1
            elif keyCode==homeR and self.homeSel<len(self.homeR)-1:
                self.homeSel+=1
            elif keyCode==awayL and self.awaySel<len(self.awayR)-1:
                self.awaySel+=1
            elif keyCode==awayR and self.awaySel>0:
                self.awaySel-=1
            
            upY,botY,north,south=40,408,273,274
            first,last=self.homeR[self.homeSel][0],self.homeR[self.homeSel][-1]
            first2,last2=self.awayR[self.awaySel][0],self.awayR[self.awaySel][-1]
            if (first.y-first.r>upY and keyCode==ord("w")) or (keyCode==ord("s") and last.y+last.r<botY):
                for row in self.homeR[self.homeSel]:
                    if keyCode==ord("w"):
                        row.y-=row.pace
                    elif(keyCode==ord("s") and last.y+last.r<botY):
                        row.y+=row.pace
            elif (keyCode==north and first2.y-first2.r>upY) or (keyCode==south and last2.y+last2.r<botY):
                for row in self.awayR[self.awaySel]:
                    if (keyCode==north):
                        row.y-=row.pace
                    elif (keyCode==south):
                        row.y+=row.pace
            shootH,shootA=301,32
            if keyCode==shootH:
                for rows in self.homeR[1:]:
                    for player in rows:
                        player.shoot(self.ball)
            elif keyCode==shootA:
                for rows in self.awayR[1:]:
                    for player in rows:
                        player.shoot(self.ball)
      
    def mousePressed(self,x,y):
        if pygame.Rect((self.pauseB)).collidepoint((x,y)):
            if not self.gameOver:
                self.paused=not self.paused
            else:
                menuSc=Exhibition()
                menuSc.run()
        elif self.ball.deadBall and pygame.Rect((self.deadBox)).collidepoint((x,y)):
                x0,y0,oVel,oAng=488,225,3,random.choice([0,180])
                self.ball.x,self.vel,self.ball.y,self.ball.angle=x0,oVel,y0,oAng
                self.ball.deadBall=False
        
    def timerFired(self, dt):
        self.ballT+=1
        if not self.paused and not self.gameOver:
            hX,aX,y1,y2,yUp,yDown=201,761,197,246 ,32,408
            self.homeSc,self.awaySc,self.paused=self.ball.isGoal(hX,aX,y1,y2,self.homeSc,self.awaySc,self.paused)
            self.ball.checkWall(hX,aX,yUp,yDown,y1,y2)
            for pos in self.homeR:
                for player in pos:
                    self.ball.checkCollision(player)
            for pos in self.awayR:
                for player in pos:
                    self.ball.checkCollision(player)
            if self.ballT%200==0:
                if int(self.matchT)>10:
                    self.matchT=str(int(self.matchT)-1)
                else:
                    self.matchT= "0"+ str(int(self.matchT)-1)
                    if self.matchT=="00":
                        self.gameOver=True
            if self.ballT%50==0:
                self.ball.ballTrack[self.ballT]=self.ball.angle
            self.ball.gravity()
            self.ball.update()
            self.homeSc,self.awaySc,self.paused=self.ball.isGoal(hX,aX,y1,y2,self.homeSc,self.awaySc,self.paused)
            self.ball.isDeadBall()
            
    def redrawAll(self,screen):
        YELLOW=(167,184,211)
        def drawInfoBoard(screen):
            startX,startY=180,440
            numTeams,dx,dy=2,30,30
            w1,h1,w2,bord=250,60,60,3
            for i in range(numTeams):
                if i==0:
                    homeB=[startX,startY,w1,h1]
                    startX+=w1+dx
                    homeScB=[startX,startY,w2,h1]
                    innH=pygame.Rect(homeB).inflate(-bord*4,-bord*4)
                    innHSc=pygame.Rect(homeScB).inflate(-bord*2,-bord*2)
                    startX+=w2+dx 
                    timeB1=[startX,startY,w1//3.4,2*h1+dy-25]
                    timeB2=[startX+w1//3.4,startY,w1//3.4,2*h1+dy-25]
                    time1In=pygame.Rect(timeB1).inflate(-bord*4,-bord*4)
                    time2In=pygame.Rect(timeB2).inflate(-bord*4,-bord*4)
                    startX+=w1//1.7+(dx-7)
                    self.pauseB=[startX,startY,w2,h1]
                    self.deadBox=[startX,startY+h1+30,w2,h1]
                    pygame.draw.rect(screen,YELLOW,self.pauseB)
                    innerB=pygame.Rect(self.pauseB).inflate(-bord*2,-bord*2)
                    pygame.draw.rect(screen,(255,255,255),innerB)
                    innerB2=pygame.Rect(self.deadBox).inflate(-bord*2,-bord*2)
                    self.playL=pygame.transform.scale(self.playL,(innerB[2]-2*bord,innerB[3]-2*bord))
                    self.pauseL=pygame.transform.scale(self.pauseL,(innerB[2]-2*bord,innerB[3]-2*bord))
                    self.exitL=pygame.transform.scale(self.exitL,(innerB[2]-2*bord,innerB[3]-2*bord))
                    self.powerB=pygame.transform.scale(self.powerB,(innerB2[2]-2*bord,innerB2[3]-2*bord))
                    if self.ball.deadBall:
                        pygame.draw.rect(screen,YELLOW,self.deadBox)
                        pygame.draw.rect(screen,(255,255,255),innerB2)
                        screen.blit(self.powerB,(innerB2[0]+bord,innerB2[1]+bord))
                    if self.paused:
                        screen.blit(self.pauseL,(innerB[0]+bord,innerB[1]+bord))
                    else:
                        if not self.gameOver:
                            screen.blit(self.playL,(innerB[0]+bord,innerB[1]+bord))
                        else:
                            screen.blit(self.exitL,(innerB[0]+bord,innerB[1]+bord))
                    pygame.draw.rect(screen,YELLOW,timeB1)
                    pygame.draw.rect(screen,(10,20,10),time1In)
                    time1=self.font2.render(self.matchT[0],False,(255,255,255))
                    screen.blit(time1,(time1In[0],time1In[1]))
                    pygame.draw.rect(screen,YELLOW,timeB2)
                    pygame.draw.rect(screen,(10,20,10),time2In)
                    time2=self.font2.render(self.matchT[1],False,(255,255,255))
                    screen.blit(time2,(time2In[0],time2In[1]))
                    pygame.draw.rect(screen,(10,20,10),homeB)
                    screen.blit(self.img1,innH[:2])
                    homeF=self.fontType.render(self.home.name,False,(255,255,255))
                    screen.blit(homeF,(innH[0],innH[1]))
                    pygame.draw.rect(screen,YELLOW,homeScB)
                    pygame.draw.rect(screen,(10,20,10),innHSc)
                    homeSc=self.font.render(str(self.homeSc),False,(255,255,255))
                    screen.blit(homeSc,(innHSc[0]+innHSc[2]/2,innHSc[1]))
                    startX-=(3*dx+w2+w1+w1//1.7-7)
                    startY+=dy+h1
                    
                elif i==1:
                    awayB=[startX,startY,w1,h1]
                    startX+=w1+dx
                    awayScB=[startX,startY,w2,h1]
                    innA=pygame.Rect(awayB).inflate(-bord*4,-bord*4)
                    innASc=pygame.Rect(awayScB).inflate(-bord*2,-bord*2)
                    pygame.draw.rect(screen,(10,20,10),awayB)
                    screen.blit(self.img1,innA[:2]) 
                    pygame.draw.rect(screen,YELLOW,awayScB)
                    pygame.draw.rect(screen,(10,20,10),innASc)
                    awayF=self.fontType.render(self.away.name,False,(255,255,255))
                    screen.blit(awayF,(innA[0],innA[1]))
                    awaySc=self.font.render(str(self.awaySc),False,(255,255,255))
                    screen.blit(awaySc,(innASc[0]+innASc[2]/2,innASc[1]))
                    startY+=dy+h1
                    startX-=(dx+w1)
                
        def drawPitch(screen):
            startX,startY=180,30
            imgW,imgH,bord=600,382,5
            pygame.draw.rect(screen,(0,0,0),[startX-bord,startY-bord,imgW+2*bord,imgH+2*bord])
            screen.blit(self.pitch,(startX,startY))
            
        def drawPlayers(screen):
            y1,y2=33,410
            if self.homeSel!=0:
                x1=self.showCurrH[self.homeSel]
                pygame.draw.line(screen,(0,0,0),(x1,y1),(x1,y2),4)
            if self.awaySel!=0:
                x2=self.showCurrA[self.awaySel]
                pygame.draw.line(screen,(255,255,255),(x2,y1),(x2,y2),4)
            for row in self.homeR:
                for player in row:
                    player.draw(screen)
            for row in self.awayR:
                for player in row:
                    player.draw(screen)
        screen.blit(self.bg,(0,0))
        drawPitch(screen)
        drawInfoBoard(screen)
        screen.blit(self.ball.img,(self.ball.x,self.ball.y))
        drawPlayers(screen)
            
class MatchStats(Screen):
    pass

class Exhibition(Screen):
    def __init__(self,width=800, height=600, fps=50, title="Exhibition",gameTeams=teams):
        super().__init__(width,height,fps,title)
        self.bg=pygame.image.load("ExhibitionBg.png")
        self.bg=pygame.transform.scale(self.bg,(self.width,self.height))
        self.teams=gameTeams
        self.currH,self.currA=0,len(self.teams)-1
        self.img=pygame.image.load("hil4.jpg")
        self.img=pygame.transform.scale(self.img,(120,60))
        self.img2=pygame.image.load("hil2.jpg")
        self.img3=pygame.image.load("hil3.jpg")
        self.img3=pygame.transform.scale(self.img3,(240,60))
        self.tact=pygame.transform.scale(self.img2,(180,40))
        self.font1=pygame.font.SysFont("Algerian",25)
        self.font2=pygame.font.SysFont("Algerian",30)
    def redrawAll(self,screen):
        YELLOW,bord=(167,184,211),10
        def leftT(screen):
            x,y,numPoints=45,60,3
            for i in range(numPoints):
                if i==0:
                   w,h,dy=140,80,30
                   homeB=[x,y,w,h]
                   homeIn=pygame.Rect(homeB).inflate(-bord*2,-bord*2)
                   hF=self.font1.render("HOME",False,(255,255,255))
                   pygame.draw.rect(screen,(10,30,10),homeB)
                   screen.blit(self.img,homeIn[:2])
                   screen.blit(hF,(homeIn[0]+20,homeIn[1]+20))
                   y+=h+dy
                elif i==1:
                    w,h,dy,marg=250,220,30,10
                    homeCr=[x,y,w,h]
                    inner=pygame.Rect(homeCr).inflate(-bord*2,-bord*2)
                    innerCr=pygame.Rect(homeCr).inflate(-bord*4,-bord*4)
                    hCr=pygame.image.load(self.teams[self.currH].logo)
                    hCr=pygame.transform.scale(hCr,innerCr[2:])
                    hCr.set_colorkey((255,255,255))
                    pygame.draw.rect(screen,(10,30,10),homeCr)
                    pygame.draw.rect(screen,(255,255,255),inner)
                    screen.blit(hCr,innerCr[:2])
                    mS=30
                    self.moveLeftH=[(x-marg,y+h//2),(x-marg-mS,y+h//2+mS//2),(x-marg,y+h//2+mS)]
                    self.moveRightH=[(x+w+marg,y+h//2),(x+w+marg+mS,y+h//2+mS//2),(x+w+marg,y+h//2+mS)]
                    pygame.draw.polygon(screen,YELLOW,self.moveRightH)
                    pygame.draw.polygon(screen,YELLOW,self.moveLeftH)
                    y+=h+dy
                else:
                    w,h,dy=250,70,30
                    homeNameB=[x,y,w,h]
                    hNBIn=pygame.Rect(homeNameB).inflate(-bord,-bord)
                    pygame.draw.rect(screen,(10,30,10),homeNameB)
                    hTeamF=self.fontType.render(self.teams[self.currH].name,False,(255,255,255))
                    screen.blit(self.img3,(hNBIn[0],hNBIn[1]))
                    screen.blit(hTeamF,(hNBIn[0],hNBIn[1]))
        def middleT(screen):
            YELLOW=(167,184,211)
            x,y,numPoints,dy,bord=355,210,7,15,5
            hT,aT=self.teams[self.currH],self.teams[self.currA]
            wearH,wearA=None,None
            for numH,kitH in enumerate(hT.kitColors):
                if not(wearH and wearA):
                    for numA,kitA  in enumerate(aT.kitColors):
                        if kitH!=kitA:
                            wearH=kitH
                            wearA=kitA
                            break
                        elif 2==numH==numA:
                            wearH=hT.kitColors[(numH+1)%len(hT.kitColors)]
                            wearA=aT.kitColors[(numA+1)%len(aT.kitColors)]
            for i in range(numPoints):
                if i%2==0:
                    w,h,pad=60,30,20
                    if i==0:
                        attB=[x+pad,y,w,h]
                        pygame.draw.rect(screen,YELLOW,attB,3)
                        y+=h+dy
                    elif i==2:
                        defB=[x+pad,y,w,h]
                        pygame.draw.rect(screen,YELLOW,defB,3)
                        y+=h+dy
                    elif i==4:
                        ovrB=[x+pad,y,w,h]
                        pygame.draw.rect(screen,YELLOW,ovrB,3)
                        y+=h+dy
                    else:
                        x,w,h,y2=310,190,50,110
                        self.playB=[x,y,w,h]
                        self.tacticsB=[x,y2,w,h]
                        playIn=pygame.Rect(self.playB).inflate(-bord*2,-bord*2)
                        tacticsIn=pygame.Rect(self.tacticsB).inflate(-bord*2,-bord*2)
                        pF=self.font2.render("PLAY",False,(255,255,255))
                        tF=self.font2.render("TACTICS",False,(255,255,255))
                        pygame.draw.rect(screen,(10,30,10),self.playB)
                        pygame.draw.rect(screen,(10,30,10),self.tacticsB)
                        screen.blit(self.tact,playIn[:2])
                        screen.blit(self.tact,tacticsIn[:2])
                        screen.blit(tF,(tacticsIn[0]+bord*4,tacticsIn[1]))
                        screen.blit(pF,(playIn[0]+bord*6,playIn[1]))
                else:
                    w,h=100,40
                    if i==1:
                        attBar=[x,y,w,h]
                        pygame.draw.rect(screen,YELLOW,attBar)
                        hW=(hT.attack+hT.pace)/2
                        aW=(aT.attack+hT.pace)/2
                        attH=[x,y,hW*w/(hW+aW),h]
                        attA=[x+hW*w/(hW+aW),y,aW*w/(hW+aW),h]
                        pygame.draw.rect(screen,wearH,attH)
                        pygame.draw.rect(screen,wearA,attA)
                        y+=dy+h
                    elif i==3:
                        defBar=[x,y,w,h]
                        pygame.draw.rect(screen,YELLOW,defBar)
                        hW=(hT.defence+hT.aggression)/2
                        aW=(aT.defence+hT.aggression)/2
                        defH=[x,y,hW*w/(hW+aW),h]
                        defA=[x+hW*w/(hW+aW),y,aW*w/(hW+aW),h]
                        pygame.draw.rect(screen,wearH,defH)
                        pygame.draw.rect(screen,wearA,defA)
                        y+=dy+h
                    else:
                        ovrBar=[x,y,w,h]
                        pygame.draw.rect(screen,YELLOW,ovrBar)
                        hW=(hT.attack+hT.ovr)/2
                        aW=(aT.attack+hT.ovr)/2
                        ovrH=[x,y,hW*w/(hW+aW),h]
                        ovrA=[x+hW*w/(hW+aW),y,aW*w/(hW+aW),h]
                        pygame.draw.rect(screen,wearH,ovrH)
                        pygame.draw.rect(screen,wearA,ovrA)
                        y+=dy+h
                   

        def rightT(screen):
            x,y,numPoints,bord=510,60,3,10
            for i in range(numPoints):
                if i==0:
                   w,h,dy,endX=140,80,30,760
                   awayB=[endX-w,y,w,h]
                   awayIn=pygame.Rect(awayB).inflate(-bord*2,-bord*2)
                   aF=self.font1.render("AWAY",False,(255,255,255))
                   pygame.draw.rect(screen,(10,30,10),awayB)
                   screen.blit(self.img,awayIn[:2])
                   screen.blit(aF,(awayIn[0]+20,awayIn[1]+20))
                   y+=h+dy
                elif i==1:
                    w,h,dy,marg,endX=250,220,30,10,760
                    awayCr=[x,y,w,h]
                    inner=pygame.Rect(awayCr).inflate(-bord*2,-bord*2)
                    innerCr=pygame.Rect(awayCr).inflate(-bord*4,-bord*4)
                    aCr=pygame.image.load(self.teams[self.currA].logo)
                    aCr=pygame.transform.scale(aCr,innerCr[2:])
                    pygame.draw.rect(screen,(10,30,10),awayCr)
                    pygame.draw.rect(screen,(255,255,255),inner)
                    screen.blit(aCr,innerCr[:2])
                    mS=30
                    self.moveLeftA=[(x-marg,y+h//2),(x-marg-mS,y+h//2+mS//2),(x-marg,y+h//2+mS)]
                    self.moveRightA=[(x+w+marg,y+h//2),(x+w+marg+mS,y+h//2+mS//2),(x+w+marg,y+h//2+mS)]
                    pygame.draw.polygon(screen,YELLOW,self.moveLeftA)
                    pygame.draw.polygon(screen,YELLOW,self.moveRightA)
                    y+=h+dy
                else:
                    w,h,dy=250,70,30
                    awayNameB=[x,y,w,h]
                    aNBIn=pygame.Rect(awayNameB).inflate(-bord,-bord)
                    pygame.draw.rect(screen,(10,30,10),awayNameB)
                    aTeamF=self.fontType.render(self.teams[self.currA].name,False,(255,255,255))
                    screen.blit(self.img3,(aNBIn[0],aNBIn[1]))
                    screen.blit(aTeamF,(aNBIn[0],aNBIn[1]))
                        
        leftT(screen)
        middleT(screen)
        rightT(screen)
    
    def mousePressed(self,x,y):
        if self.moveLeftH[2][1]>y>self.moveLeftH[0][1] and self.moveLeftH[0][0]>x>self.moveLeftH[1][0]:
            self.currH=(self.currH-1)%len(self.teams)
        elif self.moveRightH[2][1]>y>self.moveRightH[0][1] and self.moveRightH[0][0]<x<self.moveRightH[1][0]:
            self.currH=(self.currH+1)%len(self.teams)
        elif self.moveLeftA[2][1]>y>self.moveLeftA[0][1] and self.moveLeftA[0][0]>x>self.moveLeftA[1][0]:
            self.currA=(self.currA-1)%len(self.teams)
        elif self.moveRightA[2][1]>y>self.moveRightA[0][1] and self.moveRightA[0][0]<x<self.moveRightA[1][0]:
            self.currA=(self.currA+ 1)%len(self.teams)
             
        if pygame.Rect((self.playB)).collidepoint((x,y)):
            matchSc=MatchGame(self.teams[self.currH],self.teams[self.currA])
            matchSc.run()
        
        elif pygame.Rect((self.tacticsB)).collidepoint((x,y)):
            tacticsSc=Tactics(self.teams[self.currH],self.teams[self.currA])
            tacticsSc.run()
        
class Tactics(Screen):
    def __init__(self,home,away,dets=details, width=800, height=600, fps=30, title="Tactics"):
        super().__init__(width,height,fps,title)
        self.bg=pygame.image.load("Other UEFA Logo.jpg")
        self.bg=pygame.transform.scale(self.bg,(self.width,self.height))
        self.pitch=pygame.image.load("pitch2.jpg")
        self.pitch=pygame.transform.scale(self.pitch,(340,230))
        self.fH,self.fA,self.sH,self.sA=dets
        self.formH,self.styleH,=False,False
        self.formA,self.styleA=False,False
        self.home,self.away=home,away
        self.selH,self.selA=[0,0],[0,0]
        self.font2=pygame.font.SysFont("Comic Sans MS",18)
        self.pImg=pygame.image.load("hil.jpg")
        self.pImg=pygame.transform.scale(self.pImg,(94,42))
        
    def redrawAll(self,screen):
        def leftT(screen):
            self.margX,self.margY=25,25
            bord1,bord2=10,3
            startX,startY=self.margX,self.margY
            YELLOW=(167,184,211)
            numPoints=3
            for i in range(numPoints):
                if i==0:
                    dy,w,h=15,360,250
                    self.pitchH=[startX,startY,w,h]
                    self.innerPH=pygame.Rect(self.pitchH).inflate(-bord1*2,-bord1*2)
                    pygame.draw.rect(screen,(0,0,0),self.pitchH)
                    screen.blit(self.pitch,self.innerPH[:2])
                    startY+=dy+h
                elif i==1:
                    w,h,dx=130,40,20
                    formationBH=[startX,startY,w,h]
                    styleBH=[startX+w+dx,startY,w,h]
                    formationF=self.font2.render("Formation",False,(0,0,0))
                    styleF=self.font2.render("Style",False,(0,0,0))
                    x1,y1=formationBH[:2]
                    r,mar,sT,off=0.3,7,26,5
                    x2,y2=styleBH[:2]
                    self.dropDFH=[x1+(1-r)*w,y1,r*w,h]
                    self.dropDSH=[x2+(1-r)*w,y2,r*w,h]
                    x3,y3=self.dropDFH[:2]
                    x4,y4=self.dropDSH[:2]
                    clickdropDFH=[(x3+mar,y3+mar),(x3+mar+sT,y3+mar),(x3+mar+sT//2,y3+mar+sT)]
                    clickdropDSH=[(x4+mar,y4+mar),(x4+mar+sT,y4+mar),(x4+mar+sT//2,y4+mar+sT)]
                    pygame.draw.rect(screen,(255,255,255),formationBH)
                    screen.blit(formationF,(formationBH[0]+off,formationBH[1]+2*off))
                    pygame.draw.rect(screen,YELLOW,self.dropDFH)
                    pygame.draw.rect(screen,(255,255,255),styleBH)
                    screen.blit(styleF,(styleBH[0]+off,styleBH[1]+off))
                    pygame.draw.rect(screen,YELLOW,self.dropDSH)
                    pygame.draw.polygon(screen,(255,255,255),clickdropDFH)
                    pygame.draw.polygon(screen,(255,255,255),clickdropDSH)
                    startY+=dy+h
                else:
                    dx,dy,w,h,w2,h2=20,30,200,215,130,180
                    teamSBH=[startX,startY,w,h]
                    teamSBHI=pygame.Rect(teamSBH).inflate(-bord2*2,-bord2*2)
                    selPAttH=[startX+w+dx,startY,w2,h2]
                    selPAttHI=pygame.Rect(selPAttH).inflate(-bord2*3,-bord2*4)
                    pygame.draw.rect(screen,(255,255,255),teamSBH)
                    pygame.draw.rect(screen,(255,255,255),teamSBHI)
                    pygame.draw.rect(screen,(255,255,255),selPAttH)
                    pygame.draw.rect(screen,(0,0,0),selPAttHI)
                    self.home.players[self.selH[0]][self.selH[1]].drawAtt(screen,selPAttHI)
                    xP,yP,hP=startX+bord2,startY+bord2,19
                    for pos in self.home.players:
                        for player in pos:
                            player.drawBox(screen,xP,yP)
                            yP+=hP
                        
        def rightT(screen):
            endX=self.width-self.margX
            startY=self.margY
            bord1,bord2=10,3
            YELLOW=(167,184,211)
            numPoints=3
            for i in range(numPoints):
                if i==0:
                    dy,w,h=15,360,250
                    self.pitchA=[endX-w,startY,w,h]
                    self.innerPA=pygame.Rect(self.pitchA).inflate(-bord1*2,-bord1*2)
                    pygame.draw.rect(screen,(0,0,0),self.pitchA)
                    screen.blit(self.pitch,self.innerPA[:2])
                    startY+=dy+h
                elif i==1:
                    w,h,dx=130,40,20
                    formationBA=[endX-(2*w+dx),startY,w,h]
                    x1,y1,=formationBA[:2]
                    r,mar,sT,off=0.3,7,26,5
                    self.dropDFA=[x1+(1-r)*w,y1,r*w,h]
                    styleBA=[endX-w,startY,w,h]
                    formationF=self.font2.render("Formation",False,(0,0,0))
                    styleF=self.font2.render("Style",False,(0,0,0))
                    x2,y2=styleBA[:2]
                    self.dropDSA=[x2+(1-r)*w,y2,r*w,h]
                    x3,y3=self.dropDFA[:2]
                    x4,y4=self.dropDSA[:2]
                    clickdropDFA=[(x3+mar,y3+mar),(x3+mar+sT,y3+mar),(x3+mar+sT//2,y3+mar+sT)]
                    clickdropDSA=[(x4+mar,y4+mar),(x4+mar+sT,y4+mar),(x4+mar+sT//2,y4+mar+sT)]
                    pygame.draw.rect(screen,(255,255,255),formationBA)
                    screen.blit(formationF,(formationBA[0]+off,styleBA[1]+2*off))
                    pygame.draw.rect(screen,YELLOW,self.dropDFA)
                    pygame.draw.polygon(screen,(255,255,255),clickdropDFA)
                    pygame.draw.rect(screen,(255,255,255),styleBA)
                    screen.blit(styleF,(styleBA[0]+off,styleBA[1]+2*off))
                    pygame.draw.rect(screen,YELLOW,self.dropDSA)
                    pygame.draw.polygon(screen,(255,255,255),clickdropDSA)
                    startY+=dy+h
                else:
                    dx,dy,w,h,w2,h2,w3,h3=20,30,200,215,130,180,100,45
                    teamSBA=[endX-(w+dx+w2),startY,w,h]
                    playB=[endX-w3,startY+dy+h2-15,w3,h3]
                    self.playBInn=pygame.Rect(playB).inflate(-bord2*2,-bord2)
                    font3=pygame.font.SysFont("Algerian",18)
                    playF=font3.render("PLAY",False,(226,206,226))
                    selPAttA=[endX-w2,startY,w2,h2]
                    selPAttAI=pygame.Rect(selPAttA).inflate(-bord2*3,-bord2*4)
                    pygame.draw.rect(screen,(255,255,255),teamSBA)
                    pygame.draw.rect(screen,(255,255,255),selPAttA)
                    pygame.draw.rect(screen,(0,0,0),selPAttAI)
                    pygame.draw.rect(screen,(0,0,0),playB)
                    screen.blit(self.pImg,self.playBInn[:2])
                    screen.blit(playF,(self.playBInn[0]+dx,self.playBInn[1]+dx-10))
                    self.away.players[self.selA[0]][self.selA[1]].drawAtt(screen,selPAttAI)
                    xP,yP=teamSBA[0]+bord2,teamSBA[1]+bord2
                    hP=19
                    for pos in self.away.players:
                        for player in pos:
                            player.drawBox(screen,xP,yP)
                            yP+=hP
        
        def showForms(screen):
            h=25
            if self.formH:
                x,y=25,330
                for form in self.fH:
                    form.draw(screen,x,y)
                    y+=h
            if self.formA:
                x,y,=495,330
                for form in self.fA:
                    form.draw(screen,x,y)
                    y+=h
            if self.styleH:
                x,y=175,330
                for strat in self.sH:
                    strat.draw(screen,x,y)
                    y+=h
            if self.styleA:
                x,y=675,330
                for strat in self.sA:
                    strat.draw(screen,x,y)
                    y+=h
                    
        screen.blit(self.bg,(0,0))
        leftT(screen)
        rightT(screen)
        showForms(screen)
    
    def mouseMotion(self,x,y):
        if self.formH:
            for form in self.fH:
                if pygame.Rect((form.outer)).collidepoint((x,y)):
                   form.onMe=True
                else:
                    form.onMe=False
        elif self.formA:
            for form in self.fA:
                if pygame.Rect((form.outer)).collidepoint((x,y)):
                   form.onMe=True
                else:
                    form.onMe=False
        elif self.styleH:
            for strat in self.sH:
                if pygame.Rect((strat.outer)).collidepoint((x,y)):
                   strat.onMe=True
                else:
                    strat.onMe=False
        elif self.styleA:
            for strat in self.sA:
                if pygame.Rect((strat.outer)).collidepoint((x,y)):
                   strat.onMe=True
                else:
                    strat.onMe=False
        else:
            for part,pos in enumerate(self.home.players):
                for num,player in enumerate(pos):
                    if pygame.Rect(player.innBox).collidepoint((x,y)):
                        player.onMe=True
                        self.selH[0],self.selH[1]=part,num
                    else:
                        player.onMe=False
            
            for part,pos in enumerate(self.away.players):
                for num,player in enumerate(pos):
                    if pygame.Rect(player.innBox).collidepoint((x,y)):
                        player.onMe=True
                        self.selA[0],self.selA[1]=part,num
                    else:
                        player.onMe=False                           

    def mousePressed(self,x,y):
        if pygame.Rect((self.dropDFH)).collidepoint((x,y)):
            self.formH=not self.formH
        elif pygame.Rect((self.dropDFA)).collidepoint((x,y)):
            self.formA=not self.formA
        elif pygame.Rect((self.dropDSH)).collidepoint((x,y)):
            self.styleH=not self.styleH
        elif pygame.Rect((self.dropDSA)).collidepoint((x,y)):
            self.styleA=not self.styleA
        
        elif self.formH:
            for form in self.fH:
                if pygame.Rect((form.outer)).collidepoint((x,y)):
                   form.selected=True
                   self.formH=False
                else:
                    form.selected=False
        elif self.formA:
            for form in self.fA:
                if pygame.Rect((form.outer)).collidepoint((x,y)):
                   form.selected=True
                   self.formA=False
                else:
                    form.selected=False
        elif self.styleH:
            for strat in self.sH:
                if pygame.Rect((strat.outer)).collidepoint((x,y)):
                   strat.selected=True
                   self.styleH=False
                else:
                    strat.selected=False
        elif self.styleA:
            for strat in self.sA:
                if pygame.Rect((strat.outer)).collidepoint((x,y)):
                   strat.selected=True
                   self.styleA=False
                else:
                    strat.selected=False
        
        elif pygame.Rect((self.playBInn)).collidepoint((x,y)):
            matchSc=MatchGame(self.home,self.away)
            matchSc.run()
    
            
def main():
    pygame.display.set_caption('The Beginning')
    clip = VideoFileClip('trailer.mp4')
    clip=clip.resize(width=1000)
    clip.preview()
    game = Start()
    game.run()

if __name__ == '__main__':
    main()

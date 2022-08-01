import pygame
import random
import sys # to quit the game
from functions import displaytext, drawrect 

pygame.init()
width = 800
height = 600

display = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
fps = 150


def gameloop(point1,point2):
    # poing of both the players
    player1point = point1
    player2point = point2

    # all the othe stuffs
    exit = False
    distance = 20
    lineheight = 70
    player1x = 20
    player1y = height/2
    player2x = width-40
    player2y = height/2
    sizex = 20
    sizey = 100
    ballx = width/2
    bally = height/2
    randomnumber = random.randint(0,1)
    speedx = 3 if randomnumber==0 else -3
    speedy = .5 if randomnumber==0 else -.5

    while not exit:
        # events
        for e in pygame.event.get():
            keys = pygame.key.get_pressed()
            if e.type == pygame.QUIT:
                sys.exit()
            if player1y>10:
                if keys[pygame.K_w]:
                    player1y-=20
            if player1y<height-100:
                if keys[pygame.K_s]:
                    player1y+=20
            
            if player2y>10:
                if keys[pygame.K_i]:
                    player2y-=20
            if player2y<height-100:
                if keys[pygame.K_k]:
                    player2y+=20
        
        display.fill("black")

        # creating line between the screen
        for i in range(10):
            drawrect(display,"white",width/2,distance,10,70)
            distance+=(20+lineheight)
        
        distance = 10

        # player 1
        drawrect(display,"white",player1x,player1y,sizex,sizey)

        # player2
        drawrect(display,"white",player2x,player2y,sizex,sizey)

        # displaying the ball
        pygame.draw.circle(display,"purple",(ballx,bally),10)

        # checking whether player has hitted the ball or not and thereby changing the direction of the ball
        if ballx>player1x and ballx<player1x+sizex and bally>player1y-20 and bally<player1y+sizey:
            speedx=3
            if bally>player1y+sizey/2:
                speedy=2.2
            else:
                speedy=-2.2
        if ballx>player2x and ballx<player2x+sizex  and bally>player2y-20 and bally<player2y+sizey:
            speedx=-3
            if bally>player2y+sizey/2:
                speedy=2.2
            else:
                speedy=-2.2

        # changing the ball direction if satisfy the condition
        if bally>height or bally<0:
            speedy=-speedy

        ballx+=speedx
        bally+=speedy

        # displaying the score
        displaytext(display,str(player1point),width/2-100,20,50,"white",True,True)
        displaytext(display,str(player2point),width/2+100,20,50,"white",True,True)
        # global player1point,player2point
        if ballx>width:
            player1point+=1
            gameloop(player1point,player2point)
        if ballx<0:
            player2point+=1
            gameloop(player1point,player2point)

        # updating the display
        pygame.display.update()
        clock.tick(fps)



gameloop(0,0)





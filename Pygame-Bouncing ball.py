"""
#Bouncing ball using pygame
import pygame
import time
pygame.init()
screen=pygame.display.set_mode((500,300))
y=5
direction=1
counter=0
while True:
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(scree255,0,0),(250,y),12,0)
    pygame.display.update()
    time.sleep(0.005)
    if y==300:
        direction=-1
    elif y==20:
        direction=1
        counter=counter+1
    y=y+direction
    if counter==3:
        pygame.quit()
        break

#Bouncing Ball
import pygame
import time
pygame.init()
screen=pygame.display.set_mode((500,300))
y=5
direction=1
counter=0
while True:
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0),(250,y),13,0)
    pygame.display.update()
    time.sleep(0.006)
    if y==300:
        direction=-1
    elif y==5:
        direction=1
        counter+=1
    y=y+direction
    if counter==3:
        pygame.quit()
        break
"""
#Ellipse
import pygame
import time
import math
pygame.init()
screen=pygame.display.set_mode((500,300))
for _ in range(3):
    for i in range(360):
        radian=i*(math.pi/180)
        screen.fill((255,255,255))
        pygame.draw.ellipse(screen,(0,255,0),(100,100,200,40),2)
        x=math.sin(radian)*100
        y=math.cos(radian)*20
        pygame.draw.circle(screen,(255,0,0),(int(x)+200,int(y)+120),8,0)
        time.sleep(0.006)
        pygame.display.update()
pygame.quit()
    

























































        

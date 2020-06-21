import pygame
import time
import random
import math
from temp import *
pygame.init()
width=400
height=400
dis=pygame.display.set_mode((width,height))

size=10.0
#colours
green=(0,255,0)
red=(255,0,0)
black=(0,0,0)
white=(255,255,255)

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 35)

clock = pygame.time.Clock()
snake_speed=10

def printOurScore(score):
    value=score_font.render("Score  "+str(score),True,white)
    dis.blit(value,[0,0])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width/2,height/2])

def gameLoop():
    game_over=False
    x0=width/2
    y0=height/2
    snakeList=[]#this stores our snake places
    snakeList.append((x0,y0))
    snakeLength=1

    goal=(round(random.randrange(0,width-size)/10.0)*10.0,round(random.randrange(0,height-size)/10.0)*10.0)
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True

        positions=astar(snakeList,goal,height,width)#I get list of positions for our snake to go from
        print(snakeList,goal,positions)
        if positions==None:
            print("No moves found")
            game_over=True
        else:
            for position in positions:
                if position[0]>width or position[0]<0 or position[1]>height or position[1]<0:
                    game_over=True
                
                dis.fill(black)
                pygame.draw.rect(dis,red,[goal[0],goal[1],size,size])
                snakeHead=(position[0],position[1])
                
                snakeList.append(snakeHead)
                if len(snakeList)>snakeLength:
                    del snakeList[0]    
            
                if snakeHead in snakeList[:-2]:
                    print(snakeHead)
                    print("Overridden")
                    game_over=True
                
                for x in snakeList:
                        pygame.draw.rect(dis, green, [x[0], x[1], size, size])
                
                printOurScore(snakeLength)
                pygame.display.update()
                
                if position[0]==goal[0] and position[1]==goal[1]:
                    foodx=round(random.randrange(0,width-size)/10.0)*10.0
                    foody=round(random.randrange(0,height-size)/10.0)*10.0
                    while (foodx,foody) in snakeList:
                        foodx=round(random.randrange(0,width-size)/10.0)*10.0
                        foody=round(random.randrange(0,height-size)/10.0)*10.0 
                    goal=(foodx,foody)
                    snakeLength+=1
                    # snakeList.append(snakeHead)
                clock.tick(snake_speed)
    message("You lost",red)
    time.sleep(2)
    pygame.display.update()
    pygame.quit()
    quit()

gameLoop()
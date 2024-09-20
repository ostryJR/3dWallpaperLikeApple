import pygame as pg
import sys
import random as rnd
import config as cfg
import math as m

def function(x,b):
    result = 0#-m.pow(x/8,2)
    for i in b:
        if i%2==0:
            result += m.sin(i*(x+cfg.WIDTH+i/2))#*m.log(abs(x+0.01))/m.log(10)
        else:
            result += m.cos(i*(x+cfg.WIDTH+i/2))#*m.log(abs(x+0.01))/m.log(10)
    return result


def calculatePoints(scalefactor, coef):
    array = []
    
    for idx in range(-100, 100+1, 1):
        array.append([idx, function(idx,coef)-50])
    
    for idx in array: # setting the graph on the middle of the screen
        idx[0] = idx[0]*10*scalefactor + int(cfg.WIDTH/2)
        idx[1] = (idx[1]*10 + int(cfg.HEIGHT/2))*scalefactor + int(cfg.HEIGHT/1)*scalefactor
    
    array.append([cfg.WIDTH, -1])
    array.append([cfg.WIDTH, cfg.HEIGHT])
    array.append([-1, cfg.HEIGHT])
    array.append([-1, -1])
    return array



# Initialize Pygame
pg.init()
pg.font.init()

# Set up the screen
screen = pg.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
pg.display.set_caption("Testing graphs")


calculatedPointsNew = []
for i in range(0, cfg.depth):
    coef = [rnd.random() for i in range(0,10)]
    calculatedPointsNew.append(calculatePoints(1-(i*0.05), coef))


iter = 0

running = True
while running:
        
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            sys.exit(0)

    # Draw background
    screen.fill((220, 220, 220))

    for idx, line in enumerate(reversed(calculatedPointsNew)):
            #pg.draw.lines(screen,cfg.colors[idx],0,line)
            pg.draw.polygon(screen,cfg.colors[9-idx],line)


    pg.display.flip()
    iter += 1
pg.quit()
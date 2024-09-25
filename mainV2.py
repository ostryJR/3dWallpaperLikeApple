import pygame as pg
import sys
import random as rnd
import math as m
import time
import numpy as np

import config as cfg
import functions as fnc

# Initialize Pygame
pg.init()
clock = pg.time.Clock()

# Set up the screen
screen = pg.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
pg.display.set_caption(f"3D Landscape Wallpaper, set FPS:{cfg.targetFPS}, by GitHub @OstryJR, v2.0.0")


def calculatePoints(func, scale):
    result = []
    for x in range(-cfg.WIDTH, cfg.WIDTH+1, 1):
        result.append([x, cfg.functionFlat(x, func)])
    
    for idx in result: # setting the graph on the middle of the screen
        idx[0] = idx[0]*10*scale + int(cfg.WIDTH/2)
        idx[1] = (idx[1]*10 + int(cfg.HEIGHT/2))*scale + int(cfg.HEIGHT/3)*scale

    result.append([cfg.WIDTH, -1])
    result.append([cfg.WIDTH, cfg.HEIGHT])
    result.append([-1, cfg.HEIGHT])
    result.append([-1, -1])
    
    return result



#make the functions
functions = []
for i in range(0, cfg.depth):
    functions.append([rnd.random() for i in range(0,10)])
    #functions.append([rnd.randint(0,10) for i in range(0,10)])

print(functions)

running = True
while running:
    clock.tick(cfg.targetFPS)# Limit the frame rate
        
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            sys.exit(0)
    
    # Draw background
    screen.fill((220, 220, 220))
    
    #calculate points
    calculatedPoints = []
    for i in range(len(functions)-cfg.depth, len(functions)):
        calculatedPoints.append(calculatePoints(functions[i], 1-(i*0.05)))
    #print(calculatedPoints)
    
    #main code
    for idx, line in enumerate(reversed(calculatedPoints)):
        pg.draw.polygon(screen,cfg.colors[cfg.depth-idx-1].getColor(),line)
        #pg.draw.lines(screen,cfg.colors[cfg.depth-idx-1].getColor(),0,line)
   
    pg.display.flip()
pg.quit()
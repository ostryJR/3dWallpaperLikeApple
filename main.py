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
pg.font.init()

# Set up the screen
screen = pg.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
pg.display.set_caption("3d Wallpaper")

font = pg.font.SysFont(None, 36)

# Initialize Pygame clock
clock = pg.time.Clock()

calculatedPointsNew = []
for i in range(0, cfg.depth):
    calculatedPointsNew.append(fnc.calculatePoints(1-(i*0.05)))

running = True
while running:
    # Limit the frame rate to 60 FPS
    clock.tick(cfg.targetFPS)
        
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            sys.exit(0)
        
    # Draw background
    screen.fill((220, 220, 220))
    
    #main code
    
    #print colors for testing
    #for idx in range(len(cfg.colors)):
    #    pg.draw.rect(screen, (cfg.colors[idx]), (0, 0+(idx*(cfg.HEIGHT/10)), cfg.WIDTH, cfg.HEIGHT/10))
    
    
    for idx, line in enumerate(reversed(calculatedPointsNew)):
        #pg.draw.lines(screen,cfg.colors[idx],0,line)
        pg.draw.polygon(screen,cfg.colors[9-idx],line)
    #pg.draw.lines(screen,cfg.colors[1],0,calculatedPointsNew)
   
    pg.display.flip()
    i+=1
pg.quit()
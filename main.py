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
clock = pg.time.Clock()

# Set up the screen
screen = pg.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
pg.display.set_caption(f"3d Wallpaper, set FPS:{cfg.targetFPS}")
my_font = pg.font.SysFont('Roboto MS', 40)

#make the functions
functions = []
for i in range(0, cfg.depth):
    functions.append([rnd.random() for i in range(0,10)])

iter = 0

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
    
    if iter%(cfg.targetFPS*2) == 0:
        functions.append([rnd.random() for i in range(0,10)])
        iter = 0
        
    calculatedPoints = []
    for i in range(len(functions)-cfg.depth, len(functions)):
        calculatedPoints.append(fnc.calculatePoints(1-(i*0.05)+(iter/cfg.targetFPS/10), functions[i]))
    
    # Draw background
    screen.fill((220, 220, 220))
    
    #main code
    for idx, line in enumerate(reversed(calculatedPoints)):
        #pg.draw.lines(screen,cfg.colors[idx],0,line)
        pg.draw.polygon(screen,cfg.colors[cfg.depth-idx-1].getColor(),line)
        #pg.draw.lines(screen,cfg.colors[cfg.depth-idx-1].getColor(),0,line)
        
   
    pg.display.flip()
    iter += 1
pg.quit()
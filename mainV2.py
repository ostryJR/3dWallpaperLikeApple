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
pg.display.set_caption(f"3D Landscape Wallpaper, set FPS:{cfg.targetFPS}, by GitHub @OstryJR")



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
    
    
    
    #main code
    for idx, line in enumerate(reversed(calculatedPoints)):
        #pg.draw.polygon(screen,cfg.colors[cfg.depth-idx-1].getColor(),line)
        pg.draw.lines(screen,cfg.colors[cfg.depth-idx-1].getColor(),0,line)
   
    pg.display.flip()
pg.quit()
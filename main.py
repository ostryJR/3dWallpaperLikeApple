import pygame as pg
import sys
import random
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

i = 0

# Initialize Pygame clock
clock = pg.time.Clock()

calculatedPoints = fnc.calculatePoints()


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
    
    
    pg.draw.polygon(screen,cfg.colors[1],calculatedPoints)
    #pg.draw.aalines(screen,cfg.colors[1], 1, calculatedPoints)
   
    pg.display.flip()
    i+=1
pg.quit()
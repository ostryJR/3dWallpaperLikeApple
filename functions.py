import config as cfg
import math as m
import random as rnd

def calculatePoints(scalefactor):
    array = []
    for idx in range(-100, 100+1, 1):
        array.append([idx, cfg.function(idx)])
        if idx%10==0:
            print("now", idx)
    #print(array)
    
    for idx in array: # setting the graph on the middle of the screen
        idx[0] = idx[0]*10*scalefactor + int(cfg.WIDTH/2)
        idx[1] = (idx[1]*10 + int(cfg.HEIGHT/2))*scalefactor + int(cfg.HEIGHT/1)*scalefactor
    
    array.append([cfg.WIDTH, -1])
    array.append([cfg.WIDTH, cfg.HEIGHT])
    array.append([-1, cfg.HEIGHT])
    array.append([-1, -1])
    return array
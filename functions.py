import config as cfg

def calculatePoints():
    array = []
    
    for idx in range(-50, 50):
        array.append([idx, cfg.function(idx)])
    #print(array)
    
    for idx in range(len(array)):
        array[idx][0] = array[idx][0]*10 + int(cfg.WIDTH/2)
        array[idx][1] = array[idx][1]*10 + int(cfg.HEIGHT/2)+int((cfg.HEIGHT-50)/2)
    #print(array)
    array.append([1000, 0])
    array.append([1000, 1000])
    array.append([0, 1000])
    
    return array
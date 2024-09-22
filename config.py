import math as m
import random as rnd

#screen config
WIDTH = 800
HEIGHT = 600
targetFPS = 60

#function config

def function(x):
    return -(m.pow(x/4/1.5,2) + m.sin(x) + m.sin(x/3) + m.sin(x*13))

def functionNEW(x):
    return -(m.pow(x/4/1.5,2) + m.sin(x)*0.1)

def function2E(x):
    return -x*(x+6)*(2+x)*(-3-x)+3

def functionFlat(x,b):
    result = 0#-m.pow(x/30,2)
    for i in b:
        if i%2==0:
            result += m.sin(i*(x+WIDTH+i/2))
        else:
            result += m.cos(i*(x+WIDTH+i/2))
    return result

class rgb:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def getColor(self):
        return (self.r, self.g, self.b)

colors = [ # generated from https://colordesigner.io/gradient-generator/?mode=lch#292F56-E3E3E3
    rgb(41, 47, 86),
    rgb(54, 54, 92),
    rgb(66, 62, 98),
    rgb(78, 69, 104),
    rgb(89, 77, 111),
    rgb(100, 86, 117),
    rgb(110, 94, 123),
    rgb(121, 103, 130),
    rgb(131, 112, 136),
    rgb(141, 122, 143),
    rgb(150, 132, 150),
    rgb(160, 141, 157),
    rgb(169, 151, 165),
    rgb(178, 162, 172),
    rgb(187, 172, 181),
    rgb(195, 183, 189),
    rgb(203, 194, 198),
    rgb(211, 205, 207),
    rgb(219, 216, 217),
    rgb(227, 227, 227)
]

# generated from https://colordesigner.io/gradient-generator/?mode=lch#292F56-ACFA70
colors2 = [
rgb(41, 47, 86),
rgb(30, 69, 114),
rgb(0, 92, 139),
rgb(0, 116, 152),
rgb(0, 139, 160),
rgb(0, 163, 164),
rgb(0, 188, 161),
rgb(0, 212, 147),
rgb(105, 232, 130),
rgb(172, 250, 112)
]

depth = len(colors)
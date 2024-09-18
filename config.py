import math as m

#screen config
WIDTH = 800
HEIGHT = 600
targetFPS = 60
depth = 10

#function config
step = 10 #px
def functionNOTUSEDNOW(x):
    return (m.pow(x,3) + 5*m.pow(x,2) + 3*x + 2)

def function(x):
    return -m.pow(x/4,2)

colors = [
(41, 47, 86),
(30, 69, 114),
(0, 92, 139),
(0, 116, 152),
(0, 139, 160),
(0, 163, 164),
(0, 188, 161),
(0, 212, 147),
(105, 232, 130),
(172, 250, 112)
]
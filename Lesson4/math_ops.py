import math

def dist(x1,y1,x2,y2):
    dy = (y2-y1)
    dx = (x2-x1)
    return math.sqrt(dx**2+dy**2)

def sum(a,b):
    return a+b
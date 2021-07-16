from classes import *

def createmap():
    r = [room(500, 300, 300, 300), room(700, -100, 400, 400), room(800,300,300,500), room(500,600,300,200),
         room(1100,-100,200,700)]
    d = [door(750, 300, 80, r[0],r[1]), door(950,300,100,r[1],r[2]), door(650,600,80,r[0],r[3]),
         door(800,750,80,r[2],r[3],0), door(1100,400,80,r[2],r[4],0)]
    d[2].lock = 1


    return r,d

createmap()

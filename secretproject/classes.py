import sys
import math as m
import pygame
from pygame import *

class player:
    hp = 100
    inventory = []
    sinventory = []
    speed = [0,0]
    origin = heading = pygame.math.Vector2(0,-1)
    room = None
    door = None

    startimage = None
    image = None
    xy = None

    def rotate(self,x,y):
        angle = m.acos((self.xy.center[1] - y) / m.hypot(x - self.xy.center[0], y - self.xy.center[1]))
        angle = m.degrees(angle) if x < self.xy.center[0] else -m.degrees(angle)
        self.image = pygame.transform.rotate(self.startimage, angle)
        self.xy = self.image.get_rect(center=self.xy.center)
        self.heading = pygame.math.Vector2(x - self.xy.center[0], y - self.xy.center[1])

    def move(self,speed):
        movespeed = speed[:]
        if self.xy.top <= self.room.coverrect.top:
            movespeed[1] = speed[1] * (speed[1] > 0)
        if self.xy.bottom >= self.room.coverrect.bottom:
            movespeed[1] = speed[1] * (speed[1] < 0)
        if self.xy.left <= self.room.coverrect.left:
            movespeed[0] = speed[0] * (speed[0] > 0)
        if self.xy.right >= self.room.coverrect.right:
            movespeed[0] = speed[0] * (speed[0] < 0)
        return movespeed

class room:
    incolor = (150,150,150)
    wall = 5
    #wall参数为墙厚，必须为奇数
    door = set()
    #注意由构造方法定义的x,y,width,height,cover,coverrect

    def __init__(self,px,py,pwid,phei):
        self.x = px
        self.y = py
        self.width = pwid
        self.height = phei
        self.cover = pygame.Surface((self.width+self.wall, self.height+self.wall))
        self.cover.fill(self.incolor)
        self.coverrect = self.cover.get_rect()
        self.coverrect = self.coverrect.move(self.x - (self.wall - 1)/2,self.y - (self.wall - 1)/2)
        pygame.draw.rect(self.cover,(255,255,255),(int(0.5*self.wall - 0.5),int(0.5*self.wall - 0.5),self.width,self.height),self.wall)

class door:
    wall = 5
    sidea = None
    sideb = None
    lock = 0
    unlockside = None
    motion = False
    #ver 1表示竖直通行，0表示水平通行

    #定义各种情况下的颜色
    unchecked = (100,100,100)
    open = (0,255,255)
    locked = (255,0,0)

    def __init__(self,px,py,pw,sa,sb,v = 1):
        self.ver = v
        self.x = px
        self.y = py
        self.w = pw
        self.sidea = sa
        sa.door.add(self)
        self.sideb = sb
        sb.door.add(self)
        if v == 1:
            self.cover = pygame.Surface((self.w, self.wall))
            self.cover.fill(self.unchecked)
            self.coverrect = self.cover.get_rect()
            self.coverrect = self.coverrect.move(self.x - self.w / 2, self.y - (self.wall + 1) / 2)
            self.judge = pygame.Rect(self.x - self.w / 2,self.y - (self.wall + 1) / 2 - self.w * 1.2,self.w,
                                     self.wall + 2 * self.w * 1.2)

        if v == 0:
            self.cover = pygame.Surface((self.wall, self.w))
            self.cover.fill(self.unchecked)
            self.coverrect = self.cover.get_rect()
            self.coverrect = self.coverrect.move(px - (self.wall + 1) / 2, py - pw / 2)
            self.judge = pygame.Rect(self.x - (self.wall + 1) / 2 - self.w * 1.2, self.y - self.w / 2,
                                     self.wall + 2 * self.w * 1.2, self.w)









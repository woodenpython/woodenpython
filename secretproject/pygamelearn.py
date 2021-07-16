import sys
import math as m
import pygame
from pygame import *

import classes
import outstread
import createmap

#pygame 初始化
pygame.init()
size = width,height = 1280,800
screen = pygame.display.set_mode(size)
color = (0,0,0)
fps = 60

#创建玩家
tom = classes.player()
player = pygame.image.load('man.png').convert_alpha()
playerwid = 50
playerhei = 50
player = pygame.transform.scale(player,(playerwid,playerhei))
playerpo = player.get_rect()
playerpo = playerpo.move((width - playerwid)/2,(height - playerhei)/2)
tom.startimage = player
tom.xy = playerpo
speed = [0,0]
speedstep = 2   #最小速度单位
heading0 = pygame.math.Vector2(0,-1)

#加载子弹
bullet = pygame.image.load('bombfrag.png').convert_alpha()
bulletwid,bulletheight = 10,10
bullet = pygame.transform.scale(bullet, (bulletwid,bulletheight))
bullets = []    #子弹列表
bulletsdirection = []

#创建地图
room,door = createmap.createmap()
tom.room = room[0]
tom.door = door[0]
clock = pygame.time.Clock()
while True:
    clock.tick(fps)
    if tom.door.sideb.coverrect.contains(tom.xy):
        tom.room = tom.door.sideb
    if tom.door.sidea.coverrect.contains(tom.xy):
        tom.room = tom.door.sidea

    #保持中心点不动旋转
    x,y = pygame.mouse.get_pos()
    tom.rotate(x,y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                speed[1] -= speedstep
            if event.key == K_s:
                speed[1] += speedstep
            if event.key == K_d:
                speed[0] += speedstep
            if event.key == K_a:
                speed[0] -= speedstep
            if event.key == K_LSHIFT:
                speed[0] *= 2
                speed[1] *= 2
            if event.key == K_TAB:
                outstread.tabmenu(screen, fps, width, height)
            if event.key == K_f:
                for each in tom.room.door:
                    if not each.judge.contains(tom.xy):
                        pass
                    else:
                        tom.door = each
                        if each.lock == 0:
                            each.cover.fill(each.open)
                            deltaX = 0
                            deltaY = 0
                            if each.ver == 1:
                                deltaY = 2.5 * (each.coverrect.centery - tom.xy.centery)
                                # 这里采用2.2是为了保证能够通过门，而不会卡在两个房间之间
                            elif each.ver == 0:
                                deltaX = 2.5 * (each.coverrect.centerx - tom.xy.centerx)
                            clock.tick(fps)
                            screen.fill(color)
                            deltax = 0.07 * (width / 2 - x / 3 - tom.xy.center[0] * 2 / 3)
                            deltay = 0.07 * (height / 2 - y / 3 - tom.xy.center[1] * 2 / 3)
                            for every in room:
                                every.coverrect = every.coverrect.move(deltax, deltay)
                                screen.blit(every.cover, every.coverrect)
                            for every in bullets:
                                every = every.move(deltax, deltay)
                                screen.blit(bullet, every)
                            tom.xy = tom.xy.move(deltax + deltaX, deltay + deltaY)
                            for every in door:
                                every.coverrect = every.coverrect.move(deltax, deltay)
                                every.judge = every.judge.move(deltax, deltay)
                                screen.blit(every.cover, every.coverrect)
                            screen.blit(tom.image, tom.xy)
                            pygame.display.flip()
                        elif each.lock == 1:
                            each.cover.fill(each.locked)
                        break

        if event.type == KEYUP:
            if event.key == K_w:
                speed[1] = 0
            if event.key == K_s:
                speed[1] = 0
            if event.key == K_d:
                speed[0] = 0
            if event.key == K_a:
                speed[0] = 0
            if event.key == K_LSHIFT:
                speed[0] /= 2
                speed[1] /= 2

        if event.type == MOUSEBUTTONDOWN:
            temp = pygame.mouse.get_pressed()
            if temp[0]:
                heading1 = pygame.math.Vector2.normalize(tom.heading)
                bulletsdirection.append(heading1)
                position = pygame.math.Vector2(tom.xy.center[0],tom.xy.center[1])
                bulletvector = pygame.math.Vector2(bulletwid/2,bulletheight/2)
                bulletrect = bullet.get_rect()
                bulletrect = bulletrect.move(position+heading1*20-bulletvector)
                bullets.append(bulletrect)

    #子弹移动
    for i in range(len(bullets)):
        bullets[i] = bullets[i].move(12 * bulletsdirection[i])
    #子弹碰撞检测
    bulletstemp = bullets[:]
    for i in range(len(bulletstemp)):
        if bulletstemp[i].centerx > tom.room.coverrect.right or bulletstemp[i].centerx < tom.room.coverrect.left:
            bullets.remove(bullets[i])
            bulletsdirection.remove(bulletsdirection[i])
        elif bulletstemp[i].centery > tom.room.coverrect.bottom or bulletstemp[i].centery < tom.room.coverrect.top:
            bullets.remove(bullets[i])
            bulletsdirection.remove(bulletsdirection[i])

    #玩家碰撞检测
    movespeed = tom.move(speed)

    # 确定速度向量之后再移
    tom.xy = tom.xy.move(movespeed)
    #deltax,y前面的系数有很神奇的变速移动视角效果，括号内使得屏幕中心始终在角色和鼠标之间的三等分点，起到移动视角的作用
    deltax = 0.07*(width/2-x/3-tom.xy.center[0]*2/3)
    deltay = 0.07*(height/2-y/3-tom.xy.center[1]*2/3)

    #刷新画面
    screen.fill(color)
    for each in room:
        each.coverrect = each.coverrect.move(deltax,deltay)
        screen.blit(each.cover,each.coverrect)
    for each in bullets:
        each = each.move(deltax,deltay)
        screen.blit(bullet,each)
    tom.xy = tom.xy.move(deltax,deltay)
    for each in door:
        each.coverrect = each.coverrect.move(deltax, deltay)
        each.judge = each.judge.move(deltax,deltay)
        screen.blit(each.cover, each.coverrect)
    screen.blit(tom.image,tom.xy)
    pygame.display.flip()
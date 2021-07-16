import sys
import math as m
import pygame
from pygame import *
import classes

def wording(text,myfont):
    textsurf = myfont.render(text,True,(255,255,255))
    return textsurf

def tabmenu(screen,fps,wid,hei):
    clock = pygame.time.Clock()
    incolor = (255, 255, 255)
    cover = pygame.Surface((wid,hei))
    cover.fill(incolor)
    cover.set_alpha(50)
    coverrect = cover.get_rect()
    myfont = pygame.font.SysFont('arial', 50)
    word = wording("Pause", myfont)
    wordrect = word.get_rect()

    inscreen = screen
    inscreen.blit(cover, coverrect)
    inscreen.blit(word, wordrect)
    while True:
        clock.tick(fps)
        pygame.display.flip()
        for inevent in pygame.event.get():
            if inevent.type == QUIT:
                sys.exit()
            if inevent.type == KEYDOWN:
                if inevent.key == K_TAB:
                    return screen








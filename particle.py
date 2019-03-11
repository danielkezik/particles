import pygame
from math import sqrt

class Particle(pygame.sprite.Sprite):

    newvx = 0
    newvy = 0
    r = 3
    vx = 0
    vy = 0
    
    def __init__(self,x,y,weight):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.weight = weight

    def update(*args):
        self = args[0]
        scr = args[1]
        self.vx = self.newvx
        self.vy = self.newvy
        self.x += self.vx
        self.y += self.vy
        pygame.draw.circle(scr, (255,0,0), (round(self.x),round(self.y)), self.r)

    def interact(self,p):
        G = 6.67*10**(-4)
        dX = self.x-p.x
        dY = self.y-p.y
        R = sqrt(dX**2+dY**2)
        F = G*self.weight*p.weight/R**2
        self.newvx += -dX/R*F/self.weight
        self.newvy += -dY/R*F/self.weight
        p.newvx += dX/R*F/p.weight
        p.newvy += dY/R*F/p.weight

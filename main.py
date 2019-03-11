import pygame
from particle import Particle
import random as r

def main():
    pygame.init()
    screen = pygame.display.set_mode((200, 200))
    pygame.display.set_caption('Monkey Fever')
    pygame.mouse.set_visible(0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 250, 250))
    particles = [Particle(r.randint(1,200),r.randint(1,200),r.randint(1000,1001)) for i in range(10)]
    #particles[0] = Particle(100,101,100)
    #particles[1] = Particle(100, 99,100)
    pGroup = pygame.sprite.Group()
    clock = pygame.time.Clock()
    for p in particles:
        pGroup.add(p)
    while 1:
        #input()
        clock.tick(30)
        for i in range(9):
            for j in range(i+1,10):
                particles[i].interact(particles[j])
        screen.blit(background, (0, 0))
        pGroup.update(screen)
        pygame.display.flip()
        

if __name__=="__main__":
    main()

import sys
import pygame
import threading
import random
from entities import *
from thumbnails import *

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.mainloop = True
        self.basicTroops = [BasicTroop(10, random.randint(200, 400), random.randint(10, 100), x) for x in range(10)]
        self.enemy = Enemy(100, 100)
        self.alliedSprites = pygame.sprite.Group()
        self.enemySprites = pygame.sprite.Group()
        self.selectedTroops = []
        self.alliedSprites.add(self.basicTroops)
        self.mousePos = (0, 0)

    def gameloop(self):
        while self.mainloop:

            dt = self.clock.tick(60) / 1000.0
            self.screen.fill((255, 255, 255))

            for troops in self.basicTroops:
                troops.mouseControls(self.mousePos, dt)
                troops.drawCircle(self.screen)
                if troops.selected == False:
                    self.screen.blit(troops.image,(troops.x, troops.y))
                else:
                    pass

            self.screen.blit(self.enemy.image,(self.enemy.x, self.enemy.y))
            if len(self.selectedTroops) > 0:
                for troop in self.selectedTroops:
                    troop.thumbnail = btThumbnail()
                for x in range(len(self.selectedTroops)):
                    self.screen.blit(troop.thumbnail.image,(0 + (x * 32), 420))
                    self.selectedTroops[x].thumbnail.setRect(0 + (x * 32), 420)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.mainloop = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mousePos = pygame.mouse.get_pos()
                        for x in self.alliedSprites.sprites():
                            if x.rect.collidepoint(self.mousePos):
                                x.selected = True
                                if x in self.selectedTroops:
                                    pass
                                else:
                                    self.selectedTroops.append(x)
                            
                            if x.thumbnail == None:
                                pass
                            else:
                                if x.thumbnail.rect.collidepoint(self.mousePos):
                                    print(x.id)
                                    for y in self.selectedTroops:
                                        if x is y:
                                            print(x.id)
                                        else:
                                            y.selected = False
                                            y.thumbnail = None
                                            self.selectedTroops.remove(y)

                    if event.button == 3:
                        for x in self.alliedSprites.sprites():
                            x.selected = False
                            x.thumbnail = None
                            self.selectedTroops.clear()

            pygame.display.flip()

loop = Main()
loop.gameloop()
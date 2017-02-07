import pygame
import math
import os

class BasicTroop(pygame.sprite.Sprite):
    def __init__(self, speed, x, y, id):
        super(BasicTroop, self).__init__()
        self.image = pygame.image.load(os.path.join('images', 'player.png')).convert()
        self.image.set_colorkey((255,255,255))
        self.x = x
        self.y = y
        self.rect = pygame.sprite.Rect(self.x, self.y, 64, 64)
        self.speed = speed
        self.selected = False
        self.thumbnail = None
        self.id = id

    def mouseControls(self, mousePos, dt):
        if self.selected == False:
            pass
        else:
            xDistance = mousePos[0] - self.x
            yDistance = mousePos[1] - self.y
            distance = math.sqrt(xDistance * xDistance + yDistance * yDistance)
            if distance > 0:
                self.x += xDistance * self.speed * dt
                self.y += yDistance * self.speed * dt
                self.rect = pygame.sprite.Rect(self.x, self.y, 64, 64)

    def drawCircle(self, screen):
        if self.selected == True:
            elipseImage = pygame.image.load(os.path.join('images', 'selectedCircle.png')).convert()
            screen.blit(elipseImage, pygame.sprite.Rect(self.x + 10, self.y + 50, 64, 64))
            screen.blit(self.image,(self.x, self.y))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'enemy.png')).convert()
        self.image.set_colorkey((255,255,255))
        self.x = x
        self.y = y
        self.rect = pygame.sprite.Rect(self.x, self.y, 64, 64)
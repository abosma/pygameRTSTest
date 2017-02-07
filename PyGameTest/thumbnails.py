import pygame
import os

class btThumbnail(pygame.sprite.Sprite):
    def __init__(self):
        super(btThumbnail, self).__init__()
        self.image = pygame.image.load(os.path.join('images', 'basictroopSmall.png')).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

    def setRect(self, x, y):
        self.rect = pygame.sprite.Rect(x, y, 32, 32)
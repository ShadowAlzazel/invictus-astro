import pygame
from settings import *

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surface, groups, zlayer=LAYERS['main']):
        super().__init__(groups)
        self.image = surface 
        self.rect = self.image.get_rect(topleft=pos)
        self.zlayer = zlayer

class HexTile(Generic):
    def __init__(self, pos, surface, groups, zlayer=LAYERS['tiles']):
        super().__init__(pos, surface, groups)
        self.image = surface 
        self.rect = self.image.get_rect(topleft=pos)
        self.zlayer = zlayer
        
class Ship(Generic):
    def __init__(self, pos, surface, groups, zlayer=LAYERS['entity']):
        super().__init__(pos, surface, groups)
        self.image = surface 
        self.rect = self.image.get_rect(topleft=pos)
        self.zlayer = zlayer

class Projectile(Generic):
    def __init__(self, pos, surface, groups, zlayer=LAYERS['projectiles']):
        super().__init__(pos, surface, groups)
        self.image = surface 
        self.rect = self.image.get_rect(topleft=pos)
        self.zlayer = zlayer
        
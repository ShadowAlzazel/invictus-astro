import pygame
import asyncio
from settings import *

class Level: 
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        # Sprite Groups
        self.all_sprites = CameraGroup()
        # Setup
        self.setup()

    def setup(self):
        self.current_layer = LAYERS['void']

    async def run(self, dtime):
        self.display_surface.fill("Black")
        await self.all_sprites.camera_draw()
        self.all_sprites.update(dtime)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    async def camera_draw(self):
        # Each layer should be run blocking and not async
        for layer in LAYERS.values():
            self.current_layer = layer
            #render_tasks = [asyncio.create_task(self.render_sprite(sprite)) for sprite in self.sprites()]
            #done, pending = await asyncio.wait(render_tasks)

            # Note: Remove ALL async def if running this
            #for sprite in self.sprites():
            #   if sprite.zlayer == layer:
            #    self.display_surface.blit(sprite.image, sprite.rect)

    async def render_sprite(self, sprite):
        if sprite.zlayer == self.current_layer:
            self.display_surface.blit(sprite.image, sprite.rect)
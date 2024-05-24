import pygame
import sys
import asyncio
# Project modules
from settings import *
from registry import *
from ships import components
from level import Level

class Game: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Invictus: Astro")
        self.clock = pygame.time.Clock()
        self.level = Level()
        # Loader
        loader = Loader()
        # TEST
        test_path = 'data/ship/components/weapons'     
        test_class = components.WeaponComponent  
        loader.load_components(test_path, test_class)
        
        

    async def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dtime = self.clock.tick(FPS) / 1000
            await self.level.run(dtime)
            pygame.display.update()


def launch():
    game = Game()
    asyncio.run(game.run())


if __name__ == '__main__':
    launch()
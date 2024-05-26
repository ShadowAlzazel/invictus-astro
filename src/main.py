import pygame
import sys
import asyncio
# main 
from settings import *
from registry import *
from level import Level
# Project modules
from ships import components
from grid import tiles

class Game: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Invictus: Astro")
        self.clock = pygame.time.Clock()
        self.level = Level()
        # Loader
        loader = Loader()
        # -------------
        # TEST
        test_path = 'data/ship/components/weapons'     
        test_class = components.WeaponComponent  
        loader.load_components(test_path, test_class)
        new_grid = tiles.HexGrid(1)
        print(f'Grid Size: {len(new_grid.tiles)}')
        

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
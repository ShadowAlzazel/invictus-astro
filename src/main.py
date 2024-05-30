import pygame
import sys
import asyncio
# main 
from settings import *
from registry import *
from level import Level
# Project modules
from ships import components, ship
from grid import tiles, coords

class Game: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Invictus: Astro")
        self.clock = pygame.time.Clock()
        self.level = Level()
        # Loader
        loader = Loader()
        # --------------------- TEST -----------------------------
        # loading test
        test_path = 'data/ship/components/weapons'     
        test_class = components.WeaponComponent  
        loader.load_components(test_path, test_class)
        # Grid test
        new_grid = tiles.HexGrid(1)
        print(f'Grid Size: {len(new_grid.tiles)}')
        origin = new_grid.get_tile_at(qrs=[0,0,0])
        print(f'0,0,0: {new_grid.get_tile_at(qrs=[10,0,-10])}')
        print(f'Memory size: {sys.getsizeof(new_grid.mapped_tiles)}')
        hull_data = loader._import_single_obj("data/ship/hulls/hull_ZB09.json")
        hull_template = ship.HullTemplate(hull_data)
        print(f'Hull Template: {hull_template}')
        print(f'Primary Battery: {hull_template.primary_battery.slots}')
        print(f'Secondary Battery: {hull_template.secondary_battery.slots}')
        

    async def run(self):
        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
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
import pygame
import sys
import asyncio
# main 
from settings import *
from registry import *
from level import Level
# Project modules
from ships import components, ship_templates
from grid import tiles, coords

class Game: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Invictus: Astro")
        self.clock = pygame.time.Clock()
        self.level = Level()
     
    # Handle registering data from jsons
    def _register(self) -> None:
        self.data_loader = Loader()
        self.registries = RegistryAccessor()
        self.registries._register_all(self.data_loader)
        
        print(self.registries.components.members)
        # WANT
        # self.registries.components.weapons.members -> [list of weapon components]
        
        # --------------------- TEST -----------------------------
        # loading test
        #test_path = 'data/ship/components/weapons'     
        #test_class = components.WeaponComponent  
        #loader.load_components(test_path, test_class)
        # --------------------- 
        # Grid test
        #new_grid = tiles.HexGrid(1)
        #print(f'Grid Size: {len(new_grid.tiles)}')
        #origin = new_grid.get_tile_at(qrs=[0,0,0])
        # print(f'0,0,0: {new_grid.get_tile_at(qrs=[10,0,-10])}')
        #print(f'Memory size: {sys.getsizeof(new_grid.mapped_tiles)}')
        # --------------------- 
        # Hull test
        #hull_data = loader._import_single_obj("data/ship/hulls/hull_ZB09.json")
        #hull_template = ship.HullTemplate(hull_data)
        #print(f'Hull Template: {hull_template}')
        #print(f'Primary Battery: {hull_template.primary_battery.slots}')
        #print(f'Secondary Battery: {hull_template.secondary_battery.slots}')

    # main nonblocking thread 
    async def run(self):
        self._register()
        # --------------------- 
        # TEST
        hull_test = self.registries.hull_templates.get_by_key('hull_ZB09')
        print(f'Hull: {hull_test.name} | Bat: {hull_test.primary_battery}')
        lance_x2 = self.registries.components.get_by_key('lance_x2')
        
        #breakpoint()
        # --------------------- 
        # Run 
        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                    pygame.quit()
                    sys.exit()
            # tick time
            dtime = self.clock.tick(FPS) / 1000
            await self.level.run(dtime)
            pygame.display.update()


def launch() -> None:
    game = Game()
    asyncio.run(game.run())


if __name__ == '__main__':
    launch()
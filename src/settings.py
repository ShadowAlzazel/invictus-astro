from pygame.math import Vector2

# Screen
SCREEN_WIDTH = 1920
SCREEN_HEIGHT= 1080
TILE_SIZE = 64

# Framerate
FPS = 120

# Overlay 
OVERLAY_POSITIONS = {
    'hud': (40, SCREEN_HEIGHT - 15),
    'icon': (70, SCREEN_HEIGHT - 5)
}

LAYERS = {
    'void': 0, # Plain Background
    'far_space': 1, # Far background objects (far stars, galaxies, etc)
    'near_space': 2, # Near background objects (planets, stations, nebula)
    'tiles': 3, # For game tiles
    'main': 4, # Generic/Logic
    'entity': 5, # ship entity, game entity
    'projectiles': 6
}
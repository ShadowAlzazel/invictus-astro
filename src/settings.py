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
    'void': 0,
    'farspace': 1,
    'nearspace': 2,
    'ships': 3,
    'projectiles': 4
}
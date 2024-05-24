import pygame
from settings import *

# A coordinate system with 3 positions
class HexTile:
    def __init__(self, hex_coords, sprite):
        # Coords
        self.hex_coords = hex_coords
        self.q = hex_coords['q'] # UR to DL
        self.r = hex_coords['r'] # Top to Bottom
        self.s = hex_coords['s'] # UL to DR
        # Asserter
        assert self.q + self.r + self.s == 0
        
        # Neighbors
        self.neighbors = {
            'R': None,
            'L': None,
            'UR': None,
            'UL': None,
            'DR': None,
            'DL': None,
        }
        self.sprite = sprite
        
    def get_distance(self, target_hex: HexTile):
        pass
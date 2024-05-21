import pygame
from settings import *

class HexTile:
    def __init__(self, hex_coords, sprite):
        self.hex_coords = hex_coords
        self.x = hex_coords['x']
        self.y = hex_coords['y']
        self.z = hex_coords['z']
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
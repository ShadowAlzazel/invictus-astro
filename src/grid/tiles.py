import pygame
from typing import Union, Self

# Project 
from grid.coords import HexCoord

# A coordinate system with 3 positions
class HexTile:
    def __init__(self, hex_coords: HexCoord, sprite=None):
        # Coords
        self.hex_coords = hex_coords
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
        
# even sides        
class HexGrid:
    def __init__(self, size=1):
        # Generate Tiles
        self.tiles: list[HexTile] = []
        # Very basic (optimize to generate in rings)
        for q in range(-size, size + 1):
            for r in range(-size, size + 1):
                for s in range(-size, size + 1):
                    if q + r + s == 0:
                        new_hex_tile = HexTile(HexCoord([q, r, s]))
                        self.tiles.append(new_hex_tile)
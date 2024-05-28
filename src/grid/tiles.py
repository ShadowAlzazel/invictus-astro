import pygame
from typing import Union, Self, Optional

# Project 
from grid.coords import HexCoord

# A coordinate system with 3 positions
class HexTile:
    def __init__(self, hex_coords: HexCoord, sprite=None):
        # Coords (soft immutable)
        self._hex_coords = hex_coords
        self._q = self._hex_coords.q
        self._r = self._hex_coords.r
        self._s = self._hex_coords.s
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
        # List of tiles
        self.tiles: list[HexTile] = []
        # Sorted Map to HexCoord string key
        self.mapped_tiles: dict[str, HexTile] = {}
    
        # Very basic tile generator (optimize to generate in rings)
        for q in range(-size, size + 1):
            for r in range(-size, size + 1):
                for s in range(-size, size + 1):
                    if q + r + s == 0:
                        new_coord = HexCoord([q, r, s])
                        new_hex_tile = HexTile(new_coord)
                        self.tiles.append(new_hex_tile)
                        self.mapped_tiles[new_coord.coord_to_key()] = new_hex_tile
                        #print(f'Tile {q,r,s}: {new_hex_tile}')
                        
    def get_tile_at(
        self, 
        coord: Optional[HexCoord]=None,
        qrs: Optional[list[int]]=None):
        try:
            # return a tile if inputed a coord
            if coord:
                return self.mapped_tiles[coord.coord_to_key()]
            # Create key if valid coord qrs and return tile
            elif qrs:
                if len(qrs) != 3:
                    return None
                if qrs[0] + qrs[1] + qrs[2] != 0:
                    return None
                key = f'{qrs[0]}Q_{qrs[1]}R_{qrs[2]}S'
                return self.mapped_tiles[key]
            return None
        except KeyError:
            print("No Tile exists in the map with those coords.")
            return None
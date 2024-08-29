import pygame 
import json
import os
from typing import Union, Self, Optional
# Project
from ships.ship_main import Ship
from grid.tiles import HexTile, HexGrid

class ShipEntity:
    def __init__(self, ship: Ship, spawn_tile: HexTile, grid_space: HexGrid):
        # Set reference to ship
        self.ship: Ship = ship
        self.tile: HexTile = spawn_tile
        self.grid: HexGrid = grid_space
        # Combat State Paramaters
        self.is_operational: bool = True
        self.is_detected: bool = False
        self.is_revealed: bool = False
        # In-Combat Stats
        self.hit_points = ship._hit_points
        # Combat tracker
        # self.stats_tracker[damage_taken] = 0
        
    # Take Damage
    def take_damage(self, damage: int):
        self.hit_points = self.hit_points - damage
        if self.hit_points <= 0:
            self.destroy_ship()
    
    def destroy_ship(self):
        self.is_operational = False
    
    # Different sensors have differnet targeting solutions, like see through, overlap, thermal
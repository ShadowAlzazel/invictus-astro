import pygame

#JSON filename [subtype]_[manufactures]_[name]
# MAYBE CREATE DATACLASS??
class Component: 
    # A template that can be copied
    def  __init__(self, data_obj):
        self.id: str = data_obj['id']
        self.name: str = data_obj['name']
        self.size: str = data_obj['size']
        # REGISTER MANUFACTURERS FIRST (change to registry getter)
        self.manufacturer: str = data_obj['manufacturer']
        # Base stats
        self.stats: dict = data_obj['stats']
        stat_keys = self.stats.keys()
        has_stat = lambda k : k in stat_keys
        # Asserter
        if has_stat('power'):
            assert self.stats['power'] >= 0
        if has_stat('damage'):
            assert self.stats['damage'] >= 0
        if has_stat('quantity'):    
            assert isinstance(self.stats['quantity'], int)
            assert self.stats['quantity'] >= 1
            
            
    # Componet 
    # Any type of eqipment from weapons to radar to core
    
#JSON filename [subtype]_[manufactures]_[name]_[subtype_ID][Size]_[quantity]
class WeaponComponent(Component):
    def  __init__(self, data_obj):
        super().__init__(data_obj)
        assert self.stats['damage'] >= 0 # 
        assert self.stats['reload'] > 0 # No same turn shenanigans 
        assert self.stats['range'] >= 0 # *Melee weapons at 0 (same hex)
        assert self.stats['quantity'] > 0 # Needs to fire something
        
# Weapons have special attributes
# Some have travel speed 
# Some have (same tile AOE, or affects all in a tile)
# Some have tile passsthrough, ignore entities in tile besides the targeted one
# some can be intercepted 
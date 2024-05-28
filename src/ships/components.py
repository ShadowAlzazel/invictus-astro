import pygame

#JSON filename [subtype]_[manufactures]_[name]
# MAYBE CREATE DATACLASS??
class Component: 
    # A template that can be copied
    def  __init__(self, data_obj):
        self.id: str = data_obj['id']
        self.name: str = data_obj['name']
        # REGISTER MANUFACTURERS FIRST (change to registry getter)
        self.manufacturer: str = data_obj['manufacturer']
        self.stats: dict = data_obj['stats']
        # Get Stats
        stat_keys = self.stats.keys()
        in_keys = lambda k : k in stat_keys
        # Asserter
        if in_keys('power'):
            self._power = self.stats['power']
            assert self._power >= 0
        if in_keys('attack'):
            self._attack = self.stats['attack']
            assert self._attack >= 0
        if in_keys('quantity'):
            self._quantity = self.stats['attack']
            assert self._quantity >= 1
        
    # Componet 
    # Any type of eqipment from weapons to radar to core
    
#JSON filename [subtype]_[manufactures]_[name]_[subtype_ID][Size]_[quantity]
class WeaponComponent(Component):
    def  __init__(self, data_obj):
        super().__init__(data_obj)
        assert self.stats['attack'] >= 0 # 
        assert self.stats['reload'] > 0 # No same turn shenanigans 
        assert self.stats['range'] >= 0 # *Melee weapons at 0 (same hex)
        assert self.stats['quantity'] > 0 # Needs to fire something

# Some have travel speed 
# Some have (same tile AOE, or affects all in a tile)
# Some have tile passsthrough, ignore entities in tile besides the targeted one
# some can be intercepted 
import pygame

#JSON filename [subtype]_[manufactures]_[name]
class Component:
    def  __init__(self, data_obj):
        self.id = data_obj['id']
        self.name = data_obj['name']
        self.stats = data_obj['stats']
    # Componet 
    # Any type of eqipment from weapons to radar to core
    
#JSON filename [subtype]_[manufactures]_[name]_[subtype_ID][Size]_[quantity]
class Weapon(Component):
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
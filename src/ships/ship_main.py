import pygame 
import json
import os
from typing import Union, Self, Optional
# Project modules
from ships.templates import HullTemplate, ComponentSlot, SlotSet
from ships.components import Component, WeaponComponent

# Different from componenet, this holds/points a component OBJ,
# Has internal Reload/Logic
class ShipComponent:
    def  __init__(self, component: Component):
        # A reference
        self._component: Component = component 
        # Size to fit in a slot
        self.size: str = self._component.size
        # Its own instnance of stats
        self.stats: dict = self._component.stats
        stat_keys = self.stats.keys()
        has_stat = lambda k : k in stat_keys
        # Asserter
        if has_stat('power'):
            self._power: int = self.stats['power']
            assert self._power >= 0
        if has_stat('damage'):
            self._damage: int = self.stats['damage']
            assert self._damage >= 0
        if has_stat('quantity'):
            self._quantity: int = self.stats['quantity']
            assert self._quantity >= 1


# Component slots -> turn into ShipComponentSlots 
# Doesnt refrence a component slot, its another class all together
class ShipComponentSlot:    
    def __init__(self, component_slot: ComponentSlot):
        self.slot_type: str = component_slot.slot_type
        self.size: str = component_slot.size # Can hold a ShipComponent of matching size
        # Component Holder and refrence
        self.component: Optional[ShipComponent] = None
        self._is_empty: bool = True

    # Check if has a slot occupied
    def has_component(self) -> bool:
        return not self._is_empty

    # Tries to add a component to the slot return if success
    def add_component(self, component: ShipComponent) -> bool:
        # TODO: check if add a ComponentRAW
        if not self._is_empty:
            return False
        if component.size != self.size:
            return False
        if not isinstance(component, ShipComponent):
            return False
        # Success
        self._is_empty = False
        self.component = component
        return True
    
    # Replaces/Sets a component into the slot
    def set_component(self, component: ShipComponent) -> bool:
        if component.size != self.size:
            return False     
        self._is_empty = False
        self.component = component
        return True
    
    # Removes from slot amd returns if it has
    def remove_component(self) -> Optional[ShipComponent]:
        if self._is_empty:
            return None
        removed = self.component
        self.component = None
        self._is_empty = True
        return removed
    

# Set Holder for components
class ShipSlotSet:
    def __init__(self, slot_set: SlotSet):
        self.slots: dict[str, ShipComponentSlot] = {}
        self.amount: int = slot_set.amount
        # Assigner
        for key_id, slot in slot_set.slots.items():
            self.slots[key_id] = ShipComponentSlot(slot)
    
    
# Not an Entity 
class Ship:
    # Make hull to registry pointer, /DATA OBJ
    def __init__(self, name: str, asc_id: str, hull: HullTemplate, 
                 data_obj: Optional[dict]=None):
        self.name: str = name
        self.asc_id: str = asc_id # Arcus Space Command ID
        # Hull Reference
        self._hull: HullTemplate = hull # A reference do not modify
        # Primary stats
        self.stats = self._hull.stats
        self._evasion = self.stats['evasion']
        self._speed = self.stats['speed']
        self._luck = self.stats['luck']
        self._stealth = self.stats['stealth']
        self._hit_points = self.stats['hit_points']
        # Merge slot assigner and ShipComponent init here
        
        # Create slots
        self.core: ShipComponentSlot = ShipComponentSlot(hull.core)
        self.thruster: ShipComponentSlot = ShipComponentSlot(hull.thruster)
        self.sensors: ShipComponentSlot = ShipComponentSlot(hull.sensors)
        # Mapped Slot sets
        self.primary_battery: ShipSlotSet = ShipSlotSet(hull.primary_battery)

        # Create final map for slots
        self.component_slots: dict[str, ShipComponentSlot] = {}
        self.component_slots['core'] = self.core 
        self.component_slots['thruster'] = self.thruster
        self.component_slots['sensors'] = self.sensors
    
    def add_component(self, component: Component, key: str):
        new_component = ShipComponent(component)
        self.component_slots[key].add_component(new_component)
       
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
        if not self._is_empty:
            return False
        if component.size != self.size:
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
    def  __init__(self, name: str, isc_id: str, hull: HullTemplate, 
        data_obj: Optional[dict]=None):
        self.name: str = name
        self.isc_id: str = isc_id #Invictus Space Command ID
        # Hull Reference
        self._hull: HullTemplate = hull # A reference do not modify
        # Primary stats
        self.stats = self._hull.stats
        self._evasion = self.stats['evasion']
        self._speed = self.stats['speed']
        self._luck = self.stats['luck']
        self._stealth = self.stats['stealth']
        # TODO: Merge slot assigner and ShipComponent init here
        # Create Slots from hull template
        self.core = ShipComponentSlot(self._hull.core)
        self.thruster = ShipComponentSlot(self._hull.thruster)
        self.sensors = ShipComponentSlot(self._hull.sensors)
        # Mapped Slot sets
        self.primary_battery = ShipSlotSet(self._hull.primary_battery)
   
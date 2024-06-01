# A data holder 
class ComponentSlot:
    def  __init__(self, data_obj):
        self.slot_type: str = data_obj['slot_type']
        self.size: str = data_obj['size']
    # Ship Slot
    # the basic slot on a ship that accepts matching components 
    # Have different sizez, PWR usages, etc 
    # Points to a shipComponenet

    # Two main types of weapon batteries 
    # TURRETS
    # LAUNCHERS (missiles)

# Used for set of component_slots liek weapon batteries
class SlotSet:
    def  __init__(self, set_id, data_obj):
        # set vars
        provider: str = data_obj['provider']
        self._id: str = set_id
        self.amount: int = data_obj['amount']
        self.slots: dict[str, ComponentSlot] = {}
        # Asserters
        assert provider in ["list", "generator"]
        assert self.amount >= 1
        # Iterate
        if (provider == "list"):
            slot_list = data_obj['slots']
            id_list = [f'{self._id}.slot_{n}' for n in range(self.amount)]   
            assert len(slot_list) == self.amount
            assert len(id_list) == self.amount
            for slot_key, slot in zip(id_list, slot_list):
                self.slots[slot_key] = ComponentSlot(slot)
        # Generate from amount given
        elif (provider == "generator"):
            slot_sizes: str = data_obj['slot_sizes']
            slot_types: str = data_obj['slot_types']
            for n in range(self.amount):
                slot_key = f'{self._id}.slot_{n}'
                self.slots[slot_key] = ComponentSlot({"slot_type": slot_types, "size": slot_sizes})

# Template, a ship in not christened until it has its minerva
# Uneditable
class HullTemplate:
    def  __init__(self, data_obj):
        self.id: str = data_obj['id']
        self.name: str = data_obj['name']
        # REGISTER MANUFACTURERS FIRST (change to registry getter)
        self.manufacturer: str = data_obj['manufacturer']
        self.stats: dict = data_obj['stats']
        self.capacity: int = data_obj['capacity']
        # Component Slots (TODO CREATE ASSERT and safe calling)
        # Create lambda to call data_obj
        self.core = ComponentSlot(data_obj['component_slots']['core'])
        self.thruster = ComponentSlot(data_obj['component_slots']['thruster'])
        self.sensors = ComponentSlot(data_obj['component_slots']['sensors'])
        # Mapped list components
        self.primary_battery = SlotSet('primary_battery', data_obj['component_slots']['primary_battery'])
        self.secondary_battery = SlotSet('secondary_battery', data_obj['component_slots']['secondary_battery'])
        # Broadside is all or nothing on firing sequence
        self.broadside_battery = SlotSet('broadside_battery', data_obj['component_slots']['broadside_battery'])
        
        


    

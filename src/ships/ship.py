class ComponentSlot:
    def  __init__(self, data_obj):
        self.slot_type: str = data_obj['slot_type']
        self.size: str = data_obj['size']
    # Ship Slot
    # the basic slot on a ship that accepts matching components 
    # Have different sizez, PWR usages, etc 
    # Points to a shipComponenet

# Template, a ship in not christened until it has its minerva
class HullTemplate:
    def  __init__(self, data_obj):
        self.id: str = data_obj['id']
        self.name: str = data_obj['name']
        # REGISTER MANUFACTURERS FIRST (change to registry getter)
        self.manufacturer: str = data_obj['manufacturer']
        self.stats: dict = data_obj['stats']
        # Component Slots (TODO CREATE ASSERT and safe calling)
        self.component_slots = {}
        self.core = ComponentSlot(data_obj['component_slots']['core'])
        self.thruster = ComponentSlot(data_obj['component_slots']['thruster'])
        self.sensors = ComponentSlot(data_obj['component_slots']['sensors'])
        # Mapped list components
        self.primary_battery = {}
        if (data_obj['component_slots']['primary_battery']['provider'] == "list"):
            battery_list = data_obj['component_slots']['primary_battery']['battery']
            assert len(battery_list) == data_obj['component_slots']['primary_battery']['amount']
            n = 0
            for bat in battery_list:
                bat_id = f'pri_bat_{n}'
                self.primary_battery[bat_id] = ComponentSlot(bat)
                n += 1
        
    # Two main types of weapon batteries 
    # TURRETS
    # LAUNCHERS (missiles)
    def __battery_creator(self):
        pass
    
    
# Different from componenet, this holds/points a component OBJ,
# Has internal Reload/Logic
class ShipComponent:
    def  __init__(self, stats):
        self._evasion = stats['evasion']
        self._speed = stats['speed']
        self._luck = stats['luck']
        self._stealth = stats['stealth']
    
# Not an Entity 
class Ship:
    def  __init__(self, name, hull):
        self.name = name
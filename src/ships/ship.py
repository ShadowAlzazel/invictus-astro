class ComponentSlot:
    def  __init__(self):
        pass
    # Ship Slot
    # the basic slot on a ship that accepts matching components 
    # Have different sizez, PWR usages, etc 
    

# Different from componenet, this holds/points a component OBJ,
# Has internal Reload/Logic
class ShipComponent:
    def  __init__(self, stats):
        self._evasion = stats['evasion']
        self._speed = stats['speed']
        self._luck = stats['luck']
        self._stealth = stats['stealth']
    

# Template, a ship in not christened until it has its minerva
class ShipHull:
    def  __init__(self):
        pass

    
class Ship:
    def  __init__(self, name, hull):
        self.name = name


class HexCoord:
    def __init__(self, qrs: list=[0, 0, 0]):
        # list of [q, r, s]
        self.q = qrs[0] # UR to DL
        self.r = qrs[1] # Top to Bottom
        self.s = qrs[2] # UL to DR
        # A property of the coord system
        assert self.q + self.r + self.s == 0
        
    # Exhastive statemenet for getting directions in hex coord system
    def direction_vector(self, direction: str, length: int=1):
        l = length
        match direction:
            case "R": 
                return HexCoord([l, 0, -l])
            case "UR": 
                return HexCoord([l, -l, 0])
            case "UL": 
                return HexCoord([0, -l, l])
            case "L": 
                return HexCoord([-l, 0, l])
            case "DL": 
                return HexCoord([-l, l, 0])
            case "DR": 
                return HexCoord([0, l, -l])
            case _:
                return HexCoord([0, 0, 0])
            
    # Adds two hex coords and returns new hex coord
    def add_coord(self, vec):
        return HexCoord([self.q + vec.q, self.r + vec.r, self.s + vec.s])
            
    # Subtracts two hex coords and returns a new hex coord
    def sub_coord(self, vec):
        return HexCoord([self.q - vec.q, self.r - vec.r, self.s - vec.s])
            
    # Returns a new hex coord given the direction
    def add_direction(self, direction: str, length=1):
        return self.add_coord(self.direction_vector(direction, length))
    
    # Get the distance between two coords
    def get_distance(self, coord): 
        vec = self.sub_coord(coord)
        return int((abs(vec.q) + abs(vec.r) + abs(vec.s)) / 2)
    
    # Temp
    def _print_coords(self):
        return f'q:[{self.q}], r:[{self.r}], s:[{self.s}]'
    
# Test Script
if __name__ == '__main__':
    origin = HexCoord([0, 0, 0])
    move = origin.add_direction("UR", 3)
    point_1 = HexCoord([2, 0, -2])
    print(f'Origin: {origin._print_coords()}')
    print(f'Move: {move._print_coords()}')
    print(f'Distance: {origin.get_distance(origin)}')
from typing import Union, Self

class HexCoord:
    def __init__(self, qrs: list[int]):
        # list of [q, r, s]
        self.q = qrs[0] # UR to DL
        self.r = qrs[1] # Up to Down
        self.s = qrs[2] # UL to DR
        # A property of the coord system
        assert self.q + self.r + self.s == 0 # Mess with this for special levels
      
    # Used to map coords 
    def coord_to_key(self) -> str:
        return f'{self.q}Q_{self.r}R_{self.s}S'  
      
    # Exhastive statemenet for getting directions in hex coord system
    def direction_vector(self, direction: str, length: int=1) -> Self:
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
    
    # Check if same
    def are_same(self, other: Self) -> bool:
        return self.q == other.q and self.r == other.r and self.s == other.s
     
    # rounding to nearest coord (float_coords in [q,r,s] form)
    def hex_round(self, float_coords: list[int]) -> Self:
        q = round(float_coords[0])
        r = round(float_coords[1])
        s = round(float_coords[2])
        q_diff = abs(q - float_coords[0])
        r_diff = abs(r - float_coords[1])
        s_diff = abs(s - float_coords[2])
        # Check for property
        if q_diff > r_diff and q_diff > s_diff:
            q = -r - s
        elif r_diff > s_diff:
            r = -q - s
        else: 
            s = -q - r
        return HexCoord([q, r, s])
            
    # Adds two hex coords and returns new hex coord
    def add_coord(self, vec: Self) -> Self:
        return HexCoord([self.q + vec.q, self.r + vec.r, self.s + vec.s])
            
    # Subtracts two hex coords and returns a new hex coord
    def sub_coord(self, vec: Self) -> Self:
        return HexCoord([self.q - vec.q, self.r - vec.r, self.s - vec.s])
            
    # Returns a new hex coord given the direction
    def add_direction(self, direction: str, length=1) -> Self:
        return self.add_coord(self.direction_vector(direction, length))
    
    # Get the distance between two coords
    def get_distance(self, coord: Self) -> int: 
        vec = self.sub_coord(coord)
        return int((abs(vec.q) + abs(vec.r) + abs(vec.s)) / 2)
    
    # Get all coords within a distance
    def get_coords_in_range(self, dist) -> Union[Self]:
        d = int(dist) # Cast to int
        coords = []
        for q in range(-d, d + 1):
            for r in range(max(-d, -q - d), min(d, -q + d) + 1):
                s = -q - r
                coords.append(self.add_coord(HexCoord([q, r, s])))
        return coords
    
    
    
    # linear interpolation for floats
    def _lerp(self, a, b, t):
        return a + (b - a) * t
    
    # Temp
    def _print_coords(self):
        return f'q:[{self.q}], r:[{self.r}], s:[{self.s}]'
    
# Test Script
if __name__ == '__main__':
    origin = HexCoord([0, 0, 0])
    #move = origin.add_direction("UR", 3)
    #point_1 = HexCoord([2, 0, -2])
    #print(f'Origin: {origin._print_coords()}')
    #print(f'Move: {move._print_coords()}')
    #print(f'Distance: {origin.get_distance(origin)}')
    movement_range = origin.get_coords_in_range(2)
    print(f'Coords in Range: {movement_range}')
    print(f'Size: {len(movement_range)}')
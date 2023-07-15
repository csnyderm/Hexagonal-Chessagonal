import board_pieces.coordinates as coord

class Space:
    def __init__(self, q:int=None, r:int=None, s:int=None):
        if q != None and r != None and s != None:
            self.coordinates = coord.PieceCoordinates(q, r, s)
        
        else:
            self.coordinates = coord.PieceCoordinates()
        
        self.occupied = {False:None}
        self.color    = ''
    
    def __eq__(self, comparison):
        if isinstance(self, comparison.__class__):
            return self.coordinates == comparison.coordinates
        return False
    
    def get_location(self) -> tuple:
        return self.coordinates.get_coordinates()
    
    def set_space_color(self, color):
        self.color = color
    
    def is_occupied(self) -> bool:
        return self.occupied
    
    def occupy_space(self, piece):
        self.occupied = {1:piece}
    
    def unoccupy_space(self):
        self.occupied = {False:None}
    
    def calc_neighbors(self) -> set:
        neighbors = set({})
        for vector in self.coordinates.directions:
            neighbors.add(self.coordinates.add_coordinates(vector))
        #print(neighbors)
        return neighbors

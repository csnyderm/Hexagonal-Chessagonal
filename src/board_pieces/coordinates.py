# The coordinates works as follows:
# 1. The center is 0, 0, 0.

class PieceCoordinates:

    def __init__(self, q:int=None, r:int=None, s:int=None):
        if q != None and r != None and s != None:
            self.q = q
            self.r = r
            self.s = s
        
        else:
            self.q = 0
            self.r = 0
            self.s = 0
        self.directions = [(1, 0, -1), (1, -1, 0), (0, -1, 1), (-1, 0 ,1), (-1, 1, 0), (0, 1, -1)]
    
    def __eq__(self, comparison):
        if isinstance(self, comparison.__class__):
            return self.q == comparison.q and self.r == comparison.r and self.s == comparison.s
        return False
    
    def add_coordinates(self, coords:list) -> tuple:
        return (self.q + coords[0], self.r + coords[1], self.s + coords[2])
    
    def get_coordinates(self) -> tuple:
        return (self.q, self.r, self.s)
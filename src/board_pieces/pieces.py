import board_pieces.coordinates as coords
import board_pieces.space as space

class King:
    def __init__(self, init_placement:tuple):
        self.position = coords.PieceCoordinates(init_placement[0], init_placement[1], init_placement[2])
        self.moves = [(1, 0, -1), (1, -1, 0), (0, -1, 1), (-1, 0 ,1), (-1, 1, 0), (0, 1, -1), (-2, 1, 1), (2, -1, -1), (-1, 2, -1), (1, 1, -2), (-1, -1, 2), (1, -2, 1)]
    
    def calc_moves(self) -> set:
        neighbors = set({})
        for vector in self.moves:
            neighbors.add(self.moves(vector))
        #print(neighbors)
        return neighbors
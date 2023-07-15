
import board_pieces.space as space
import board_pieces.game_board as board

global BOARD_SIZE
BOARD_SIZE = 5

starting_space = space.Space()
game_board = {starting_space.get_location():starting_space}
game_board = board.create_game_board({starting_space.get_location()}, game_board, BOARD_SIZE)

print(game_board)
print(len(game_board))

game = {}
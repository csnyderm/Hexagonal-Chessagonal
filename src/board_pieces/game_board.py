import board_pieces.space as space

def reset_game_board(game_board:list) -> set:
    for space in game_board:
        space.unoccupy_space()
    return game_board

def find_outward_neighbors(known_spaces:set, game_board:dict, BOARD_SIZE:int) -> tuple:
    """Find next outward neighbors, and add them to the gameboard"""
    all_neighbors = []
    relevant_neighbors = set({})
    
    # Generate all of our neighbors at once into a list
    for hex in known_spaces:
        board_space = space.Space(hex[0], hex[1], hex[2])
        all_neighbors.append(board_space.calc_neighbors())
    
    # Parse through list and union all sets into one big set
    for neighbor in all_neighbors:
        relevant_neighbors = relevant_neighbors.union(neighbor)
    
    # Remove any that already exist in the game board
    relevant_neighbors = relevant_neighbors.difference(set(game_board.keys()))
    
    # Just in case, if we have any that go above the board size, throw them out
    for neighbor in relevant_neighbors:
        if (BOARD_SIZE+1) in neighbor:
            relevant_neighbors.discard(neighbor)
        
        board_space = space.Space(neighbor[0], neighbor[1], neighbor[2])
        game_board[neighbor] = board_space
    
    return game_board, relevant_neighbors

def create_game_board(known_spaces:set, game_board:dict, BOARD_SIZE:int):
    
    for i in range(BOARD_SIZE):
        neighbor_tuple = find_outward_neighbors(known_spaces, game_board, BOARD_SIZE)
        known_spaces = neighbor_tuple[1]
        game_board = neighbor_tuple[0]
    
    return game_board
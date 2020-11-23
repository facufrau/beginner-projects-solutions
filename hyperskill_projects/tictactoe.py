# Read input from user
user_moves = input("Enter cells: ")

def print_board(moves):
    """
    Prints the board from a list of moves.
    """
    print("---------")
    for i in range(0, 8, 3):
        print(f"| {moves[i + 0]} {moves[i + 1]} {moves[i + 2]} |")
    print("---------")

print_board(user_moves)
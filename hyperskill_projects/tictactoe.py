# Read input from user
user_moves = input("Enter cells: ")

def print_board(moves):
    """
    Prints the board from a list of moves.
    """
    print("---------")
    print(f"| {moves[0]} {moves[1]} {moves[2]} |")
    print(f"| {moves[3]} {moves[4]} {moves[5]} |")
    print(f"| {moves[6]} {moves[7]} {moves[8]} |")
    print("---------")

print_board(user_moves)
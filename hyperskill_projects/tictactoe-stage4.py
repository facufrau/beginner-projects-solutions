def print_board(moves):
    """
    Prints the board from a list of moves.
    """
    print("---------")
    for i in range(0, 8, 3):
        print(f"| {moves[i + 0]} {moves[i + 1]} {moves[i + 2]} |")
    print("---------")

def count_moves(moves):
    """
    Counts the amount of X and O in the board.
    """
    x_qty = moves.count("X")
    o_qty = moves.count("O")
    return x_qty, o_qty

def rows_wins(moves):
    """
    Count the amount of rows completed with 3 of a kind(X,O)
    The rows are based in a 3x3 grid with 0 in left top number.
    Empty cell is represented with '_'
    """
    rows = [[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[0,4,2]]
    winned = 0
    won = ''
    for row in rows:
        if (moves[row[0]] != '_') and (moves[row[0]] == moves[row[1]]):
            if moves[row[1]] == moves[row[2]]:
                winned += 1
                won = moves[row[0]]  # 'X' or 'O'
    return winned, won

def check_state(moves):
    """
    Check the state of the board from a list of moves.
    Prints X/O wins, draw, game not finished or impossible.
    """
    x, o = count_moves(moves)
    total_moves = x + o
    if abs(x - o) >= 2:
        return "Impossible"
    else:
        winned, won = rows_wins(moves)
        if winned == 0:
            if total_moves == 9:
                return "Draw"
            else:
                return "Game not finished"
        elif winned == 1:
            return won + ' wins'
        else:
            return "Impossible"
        
def update_board(moves, i, mark):
    """
    Updates the moves list with the provided index and mark.
    Returns True if the space was free, false if occupied.
    """
    if moves[i] == '_':
        moves[i] = mark
        return True
    else:
        return False

def main():
    user_moves = list(input("Enter cells: "))
    print_board(user_moves)
    #result = check_state(user_moves)
    #print(result)

    while True:
        coords = input("Enter the coordinates: ").split()
        try:
            coords = [int(x) for x in coords]
            col , row = coords[1], coords[0]
        except:
            print("You should enter numbers!")
            continue

        if (1 <= row <= 3) and (1 <= col <=3):
            index  = ((3 - col) * 3) + (row - 1)  # Convert coordinates to list index.
            mark = 'X'
            if update_board(user_moves, index, mark):
                print_board(user_moves)
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue

if __name__ == "__main__":
    main()
example_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def print_board(board):
    """Printout a board"""

    for row in range(len(board)):
        if row % 3 == 0:
            print(" | - - - - - - - - - - - - | ")

        for column in range(len(board[0])):
            if column % 3 == 0:
                print(" | ", end="")

            if column == 8:
                print(str(board[row][column]) + " | ")
            else:
                print(str(board[row][column]) + " ", end="")
    print(" | - - - - - - - - - - - - |")


def find_empty(board):
    """Find all the empty spaces a.k.a. 0"""

    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return row, column

    return None

def valid(board, number, position):
    """Check the validity of the board"""

    # Check the same row
    for column in range(len(board[0])):
        if board[position[0]][column] == number and position[1] != column:
            return False

    # Check the same column
    for row in range(len(board)):
        if board[row][position[1]] == number and position[0] != row:
            return False

    # Check the square
    square_x = position[1] // 3
    square_y = position[0] // 3

    for row in range(square_y * 3, square_y * 3 + 3):
        for column in range(square_x * 3, square_x * 3 + 3):
            if board[row][column] == number and (row,column) != position:
                return False

    return True

def solve(board):
    """Recursive algorithm"""

    # Checks if there are any more empty spaces, if not then solved
    empty = find_empty(board)
    if not empty:
        return True
    else:
        row, column = empty

    # Try all possible numbers, if valid replace the 0
    for number in range(1,10):
        if valid(board, number, (row, column)):
            board[row][column] = number

            # Recursive calling
            if solve(board):
                return True
            # If stuck then take a step back
            board[row][column] = 0

    return False

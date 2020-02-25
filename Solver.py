def print_board(board):
    """
    Prints a visual representation of the board.
    :param board: 2d list 9x9
    :return: visual representation
    """

    # Iterating over each row of the board
    for row in range(len(board)):

        # Printing in-between rows of the board
        if row % 3 == 0 and row != 0:
            print("-----------------------")

        # Iterating over each column of the board
        for column in range(len(board[0])):

            # Printing in-between columns of the board
            if column % 3 == 0 and column != 0:
                print(" | ", end="")

            # Printing elements
            if column == 8:
                print(board[row][column])
            else:
                print(str(board[row][column]) + " ", end="")


def find_empty(board):
    """
    Finds the first empty square on the board.
    :param board: 2d list 9x9
    :return: tuple (row, column)
    """

    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return row, column
    return None


def valid(board, value, position):
    """
    Checks if value can be put in said position on said board
    :param board: 2d list 9x9
    :param value: positive integer (1-9)
    :param position: tuple (row, column)
    :return: boolean
    """

    # Checking row
    for i in range(len(board[0])):
        if board[position[0]][i] == value and position[1] != i:
            return False

    # Checking column
    for i in range(len(board)):
        if board[i][position[1]] == value and position[0] != i:
            return False

    # Checking squares
    box_x = position[1] // 3
    box_y = position[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == value and (i, j) != position:
                return False

    return True  # If all tests are passed, it is valid


def solver(board):
    """
    Solves the board using a backtrack algorithm
    :param board: 2d list 9x9
    :return: boolean
    """

    find = find_empty(board)

    # Base case (when all positions are completed and has reached the end of the board)
    if not find:
        return True

    # Recursive case (still solving the board)
    else:
        row, column = find  # Found an empty position

    # Iterating over each number 1 through 9
    for i in range(1, 10):

        if valid(board, i, (row, column)):
            board[row][column] = i  # Adding value to the board

            if solver(board):
                return True  # Finishes solving

            board[row][column] = 0  # Resets values so that we can backtrack it

    return False  # Used to initialize the backtracking process


board_example = [
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

print_board(board_example)
solver(board_example)
print()
print("SOLVING BOARD...")
print()
print_board(board_example)

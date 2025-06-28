import numpy as np

columns = int(input(" enter number of columns: "))
rows = int(input(" enter number of rows: "))


def display_board(board):
    for i in range(rows):
        print(" ---" * columns)
        print("| " + " | ".join(board[i]) + " |")
    print(" ---" * columns)


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True

    # Check columns
    for col in range(columns):
        if all(board[row][col] == player for row in range(rows)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(rows)):
        return True
    if all(board[i][columns - 1 - i] == player for i in range(rows)):
        return True

    return False


def moves():
    board = [[" " for _ in range(columns)] for _ in range(rows)]
    print("DISCLAIMER: THE FIRST ROW AND COLUMN WILL BE = 0, AND THE SECOND ONE WILL BE = 1, AND SO ON.")

    while True:
        if is_board_full(board):
            print("Board is full. It's a draw!")
            break

        for player in ['x', 'y']:
            while True:
                print(f"Player {player} turn ({player})")
                row_move = int(input("Which row would you like to move (its the horizontal one): "))
                columns_move = int(input("Which columns would you like to move (its the vertical one): "))

                if board[row_move][columns_move] == " ":
                    board[row_move][columns_move] = player
                    display_board(board)
                    if check_winner(board, player):
                        print(f"Player {player} wins!")
                        return
                    break
                else:
                    print("Invalid move. Try again.")


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


moves()

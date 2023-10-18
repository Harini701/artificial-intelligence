def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    if col == len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_n_queens(board, col + 1):
                return True

            board[i][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
        print()

def solve_8_queens():
    n = 8
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0):
        print("Solution:")
        print_board(board)
    else:
        print("No solution found.")

if __name__ == "__main__":
    solve_8_queens()

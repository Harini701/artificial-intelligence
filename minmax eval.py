def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):
        return -1
    if check_win(board, "O"):
        return 1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_eval = -float("inf")
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                eval = minimax(board, 0, False)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe Game")
    print_board(board)

    while True:
        while True:
            move = input("Enter your move (row[1-3] column[1-3]): ")
            try:
                row, col = map(int, move.split())
                if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter your move as 'row[1-3] column[1-3]'.")

        board[row - 1][col - 1] = "X"
        print_board(board)

        if check_win(board, "X"):
            print("You win!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = "O"
        print("Computer's move:")
        print_board(board)

        if check_win(board, "O"):
            print("Computer wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()

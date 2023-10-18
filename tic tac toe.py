def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    # Check if the board is full (a tie)
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Tic Tac Toe Game")
    print_board(board)

    while True:
        while True:
            move = input(f"Player {player}, enter your move (row[1-3] column[1-3]): ")
            try:
                row, col = map(int, move.split())
                if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter your move as 'row[1-3] column[1-3]'.")

        board[row - 1][col - 1] = player
        print_board(board)

        if check_win(board, player):
            print(f"Player {player} wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    main()

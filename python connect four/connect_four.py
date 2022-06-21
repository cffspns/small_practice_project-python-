from os import system
from time import sleep

def intro():
    print("Welcome to Connect Four!")
    print("Player 1 uses Xs, Player 2 uses Os. Get 4-in-a-row to win!")
    sleep(2)

def clr():
    system("cls||clear")
    
def print_board(board):
    sep_one = "+" + ("---+" * 7)
    sep_two = "|" + ("   |" * 7)
    print("  1   2   3   4   5   6   7  ")
    print(sep_one)
    for i in range(5, -1, -1):
        print(sep_two)
        print(f"| {board[0][i]} | {board[1][i]} | {board[2][i]} | {board[3][i]} | {board[4][i]} | {board[5][i]} | {board[6][i]} |")
        print(sep_two)
        print(sep_one)

def switch_player(player):
    return 1 if player == 0 else 0

def check_full(board):
    for column in board:
        if ' ' in column:
            return False
    return True

def check_win(board):
    # Horizontal check
    for col in range(4):
        for row in range(6):
            if board[col][row] != ' ' and (board[col][row] == board[col+1][row] == board[col+2][row] == board[col+3][row]):
                return True
    # Vertical check
    for col in range(6):
        for row in range(3):
            if board[col][row] != ' ' and (board[col][row] == board[col][row+1] == board[col][row+2] == board[col][row+3]):
                return True
    # Positive Diagonal check
    for col in range(4):
        for row in range(3):
            if board[col][row] != ' ' and (board[col][row] == board[col+1][row+1] == board[col+2][row+2] == board[col+3][row+3]):
                return True
    # Negative Diagonal check
    for col in range(4):
        for row in range(5, 2, -1):
            if board[col][row] != ' ' and (board[col][row] == board[col+1][row-1] == board[col+2][row-2] == board[col+3][row-3]):
                return True
    return False


def game_loop():
    pieces = "XO"
    current_player = 1
    board = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    while True:
        clr()
        print_board(board)
        if check_win(board):
            print(f"Game over! Player {current_player+1} wins!")
            break
        elif check_full(board):
            print("Game over! It's a draw :(")
            break
        else:
            current_player = switch_player(current_player)
            print(f"It's player {current_player+1}'s turn!")
            while True:
                move = input("Enter a number from 1 to 7 to drop a piece in that column!: ")
                if move not in ["1", "2", "3", "4", "5", "6", "7"]:
                    print("That's not a valid input! Try again!")
                    continue
                elif ' ' not in board[int(move)-1]:
                    print("That column appears to be full! Try again!")
                    continue
                else:
                    for idx in range(6):
                        if board[int(move)-1][idx] == ' ':
                            board[int(move)-1][idx] = pieces[current_player]
                            break
                    break
        

def game():
    clr()
    intro()
    game_loop()


game()
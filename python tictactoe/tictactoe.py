# Tic Tac Toe! A python terminal game for 2 players
from os import system
from time import sleep

def print_board(board):
    row_one = board[0] + "|" + board[1] + "|" + board[2]
    row_two = board[3] + "|" + board[4] + "|" + board[5]
    row_three = board[6] + "|" + board[7] + "|" + board[8]
    row_sep = "-----"
    print(row_one)
    print(row_sep)
    print(row_two)
    print(row_sep)
    print(row_three)

def switch_turn(current_turn):
    if current_turn == 1:
        return 2
    else:
        return 1

def check_win(board):
    row_one = board[0] == board[1] and board[0] == board[2] and board[0] != " "
    row_two = board[3] == board[4] and board[3] == board[5] and board[3] != " "
    row_three = board[6] == board[7] and board[6] == board[8] and board[6] != " "
    col_one = board[0] == board[3] and board[0] == board[6] and board[0] != " "
    col_two = board[1] == board[4] and board[1] == board[7] and board[1] != " "
    col_three = board[2] == board[5] and board[2] == board[8] and board[2] != " "
    dia_one = board[0] == board[4] and board[0] == board[8] and board[0] != " "
    dia_two = board[2] == board[4] and board[2] == board[6] and board[2] != " "
    if any([row_one, row_two, row_three, col_one, col_two, col_three, dia_one, dia_two]):
        return True
    return False

def check_full(board):
    for position in board:
        if position == " ":
            return False
    return True

def validate_input(user_input):
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return user_input in digits

def turn(current_turn, board, counters):
    system("cls||clear")
    print_board(board)
    print(f"It's player {current_turn}'s turn!")
    valid_move = False
    while not valid_move:
        cell_choice = input("Pick a cell! (1-9, 1 at the top-left, 9 at the bottom-right): ")
        if not validate_input(cell_choice):
            print("That's not a valid choice! Try again!")
            continue
        cell_choice = int(cell_choice)
        if board[cell_choice - 1] != " ":
            print("That cell is filled! Try again!")
            continue
        board[cell_choice - 1] = counters[current_turn]
        valid_move = True

def game_over(current_turn, board):
    if check_win(board):
        print(f"Game over! Player {current_turn} wins! :)")
    else:
        print("Game over! It's a draw :(")


def game():
    board = [" " for i in range(9)]
    counters = {1: "X", 2: "O"}
    current_turn = 2

    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 has the Xs, player 2 has the Os. First to three in a row wins!")
    sleep(2)

    while not check_win(board) and not check_full(board):
        current_turn = switch_turn(current_turn)
        turn(current_turn, board, counters)
    game_over(current_turn, board)

game()
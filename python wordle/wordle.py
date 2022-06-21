from wordlist import answer_list, allowed_list
from random import choice
from os import system
from time import sleep

hard_mode = False

def intro():
    print("Welcome to wordle! (kind of)")
    while True:
        difficulty = input("Currently in normal mode. Change to hard mode? (Y/N) ").lower()
        if difficulty == 'y':
            print("Difficulty changed to hard mode!")
            hard_mode = True # Currently makes no difference
            break
        elif difficulty == 'n':
            print('Difficulty set to normal mode!')
            break
        else:
            print('Invalid input! Please input Y or N (case insensitive).')

def result(answer, guess):
    # X = miss, ? = right-letter-wrong-position, ! = correct
    result = [None for _ in range(5)]
    answer = list(answer)
    guess =  list(guess)
    # Handle check for correct guesses and right-letter-wrong-position/misses in two seperate loops to handle some edge cases
    for idx in range(5): 
        if guess[idx] == answer[idx]:
            result[idx] = ("!")
            guess[idx] = answer[idx] = None
    for idx in range(5):
        if guess[idx] is None:
            continue
        if guess[idx] not in answer:
           result[idx] = "X"
        else:
            result[idx] = "?"
            position = answer.index(guess[idx])
            answer[position] = None
    return " ".join(result)

def game_loop():
    answer = choice(answer_list)
    guess_list = []
    result_list = []
    guess_count = 0
    while guess_count < 6:
        system("cls||clear")
        for idx, word in enumerate(guess_list):
            print(f"{' '.join(list(word.upper()))}")
            print(f"{result_list[idx]}")
        guess = input(f"You have {6 - guess_count} {'try' if guess_count == 5 else 'tries'} left. Guess a 5-letter word: ")
        if guess not in answer_list and guess not in allowed_list:
            print("Looks like that isn't a recognised word. Try again!")
            sleep(2)
            continue
        if guess in guess_list:
            print("You've already guessed that word! Maybe try something else?")
            sleep(2)
            continue
        guess_count += 1
        guess_list.append(guess)
        result_list.append(result(answer, guess))
        if guess == answer:
            print("Correct, you win!")
            return
    print("You are out of tries! You lose :(")
    print(f"The word was: {answer}")

def wordle():
    intro()
    game_loop()

wordle()
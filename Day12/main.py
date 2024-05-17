import random

EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5


def check_answer(user_guess, com_guess, number_of_try):
    if user_guess > com_guess:
        print("Too high, Try again")
        return number_of_try - 1
    elif user_guess < com_guess:
        print("Too low, Try again.")
        return number_of_try - 1
    else:
        print(f"Correct!!!. The answer is {com_guess}")


def set_difficulty():
    level = input("Choose difficulty, easy or hard: \n")
    if level == "easy":
        return EASY_LEVEL_LIVES
    else:
        return HARD_LEVEL_LIVES


def game():
    print("WELCOME TO THE GAME!!!")
    print("I'm thinking of a number from 1 to 100")

    answer = random.randint(1, 100)
    print(answer)

    number_of_try = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"you have {number_of_try} guess remaining!")
        guess = int(input("Guess a number!!!: \n"))
        number_of_try = check_answer(guess, answer, number_of_try)
        if number_of_try == 0:
            print("YOU LOOSE. OUT OF GUESSES!")
            return
        elif guess != answer:
            print("guess again!")



game()





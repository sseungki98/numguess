from random import randint
from time import sleep

# get username and greeting
def get_username():
    username = input("What is your name? > ")
    print(f"Welcome, {username}!")
    return username

# get userguess and print
def get_userguess():
    user_guess = int(input("What is your guess?(1~100) > "))
    print(f"Your guess is {user_guess}, right?")
    return user_guess

# check user_guess with answer
def check_answer(answer, user_guess):
    if answer == user_guess:
        print('******************************')
        print('Congratulation !! Correct !!')
        print('******************************')
        return
    elif user_guess > answer:
        print("Sorry, you are wrong... answer is lower than your guess.")
    else:
        print("Sorry, you are wrong... answer is higher than your guess.")

def play_game():
    username = get_username()
    answer = randint(1,100)
    user_guess = get_userguess()
    check_answer(answer,user_guess)
    print(f"Answer is {answer}!")

play_game()

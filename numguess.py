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
        return True
    elif user_guess > answer:
        print("Sorry, you are wrong... answer is lower than your guess.")
        return False
    else:
        print("Sorry, you are wrong... answer is higher than your guess.")
        return False

def play_game(total_score, try_count):
    score = 100
    username = get_username()
    answer = randint(1,100)
    while(True):
        user_guess = get_userguess()
        status = check_answer(answer,user_guess)
        if status:
            break
        score -= 5
    print(f"Answer is {answer}!")
    print(f"You Got {score} points!!")
    total_score += score
    print(f"Your Try count is {try_count}, and Total score is {total_score} points")
    choice = input("Do you want to play this game again?(Y/N) ( want to play, Press Y. want to quit, Press N) > ")
    if choice == 'Y':
        try_count += 1
        return play_game(total_score, try_count)
    else:
        return

total_score = 0
try_count = 1
play_game(total_score, try_count)

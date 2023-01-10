from random import randint
from time import sleep

# Get user's name
username = input("What is your name? > ")

# Greet user 
print(f"Welcome, {username}!")

# Generate random answer
answer = randint(1,100)

# Get user's guess
user_guess = input("What is your guess? > ")

# Print user's guess
print(f"Your guess is {user_guess}, right?")

# Print answer number
print(f"Answer is {answer} !")

# Compare user's guess with answer
if user_guess == answer:
    print('*****************************')
    sleep(1)
    print('*****************************')
    sleep(1)
    print('*****************************')
    sleep(1)
    print("Wow, Correct!")
else:
    print("Sorry, You are wrong...")


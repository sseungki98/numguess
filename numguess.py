from random import randint

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



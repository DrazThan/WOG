import random

def generate_number(user_difficulty_select):
    random_number = random.randint(0,int(user_difficulty_select))
    return random_number

def get_guess_user(user_difficulty_select):
    user_guess = input(f"please enter a random number from 0 to {user_difficulty_select} ")
    print(f"You selected the number {user_guess}")
    return int(user_guess)

def compare_results(user_guess,random_number):
    if user_guess == random_number:
        print ("You are correct")
    else: print(f"You failed, the number was {random_number}")
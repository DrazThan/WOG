# memory_game.py
import os
import time
import random
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')



def generate_sequence(number_of_elements):
    random_list = []
    for _ in range(number_of_elements):
        try:
            random_number = random.randint(1, 100)
        except Exception as e:
            print(f"An error has occured while generating a random number: {e}")
            return []
        print(random_number, end=' ')
        random_list.append(random_number)
    time.sleep(1)
    clear_screen()
    return random_list

def get_list_from_user():
    while True:
        try:
            user_input = input("Please enter the numbers you saw, seperated by commas:  ")
            user_list = user_input.split(',')
            user_list = [int(i) for i in user_list]
            return user_list
        except ValueError:
            print("Invalid input. please only enter numbers seperated by commas")

def is_list_equal(user_list,random_list):
    if user_list == random_list :
        print ("You are correct")
    else:
        print("You failed")

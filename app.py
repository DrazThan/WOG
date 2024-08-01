from score import add_score
from currency_roulette_game import play_currency_roulette
from memory_game import generate_sequence,get_list_from_user,is_list_equal
from guess_game import generate_number, get_guess_user, compare_results


# This file acts as the main menu and entry point for the games.

def welcome():
    user_name_input = input("Please Enter Your Username: ")
    print(f"Hi {user_name_input} and welcome to the World of Games: The Epic Journey")
    return user_name_input

def start_play():
    game_select = {
        1: "Memory Game",
        2: "Guess Game",
        3: "Currency Roulette"
    }
    user_game_select_string = input("""Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
2. Guess Game - guess a number and see if you chose like the computer.
3. Currency Roulette - try and guess the value of a random amount of USD in ILS 
Your choice: """)
    user_game_select = int(user_game_select_string)
    
    while user_game_select not in game_select:
        print("Invalid selection. Please choose a valid game.")
        user_game_select = input("Please choose a game to play (1, 2, or 3): ")
    
    user_difficulty_select = input("Thank you for selecting the game, please select a difficulty of 1-5: ")
    
    while not user_difficulty_select.isdigit() or not (1 <= int(user_difficulty_select) <= 5):
        print("Invalid difficulty level. Please select a number between 1 and 5.")
        user_difficulty_select = input("Please select a difficulty of 1-5: ")
    
    print(f"You have selected {game_select[user_game_select]} with Difficulty {user_difficulty_select}")
    return user_game_select, user_difficulty_select

def main_menu():
    user_name = welcome()
    while True:
        game,user_difficulty_select = start_play()
        if game == 2:
            random_number = generate_number(user_difficulty_select)
            user_guess = get_guess_user(user_difficulty_select)
            user_wins = compare_results(user_guess, random_number)

        elif game == 1:
            random_list = generate_sequence(int(user_difficulty_select))
            user_list = get_list_from_user()    
            user_wins = is_list_equal(user_list,random_list)
        elif game == 3:
            user_wins = play_currency_roulette(user_difficulty_select)
        if user_wins:
            add_score(user_difficulty_select)
        
        play_again = input("Do you want to play another game? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing! See you next time.")
            break  # Exit the loop and end the program

if __name__ == "__main__":
    main_menu()
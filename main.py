# main.py

from games import play
from score import add_score

def welcome():
    user_name = input("Please Enter Your Username: ")
    print(f"Hi {user_name} and welcome to the World of Games: The Epic Journey")
    return user_name

def start_play():
    game_select = {
        1: "Memory Game",
        2: "Guess Game",
        3: "Currency Roulette"
    }
    user_game_select = int(input("""Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
2. Guess Game - guess a number and see if you chose like the computer.
3. Currency Roulette - try and guess the value of a random amount of USD in ILS 
Your choice: """))
    
    while user_game_select not in game_select:
        print("Invalid selection. Please choose a valid game.")
        user_game_select = int(input("Please choose a game to play (1, 2, or 3): "))
    
    user_difficulty_select = int(input("Thank you for selecting the game, please select a difficulty of 1-5: "))
    
    while not (1 <= user_difficulty_select <= 5):
        print("Invalid difficulty level. Please select a number between 1 and 5.")
        user_difficulty_select = int(input("Please select a difficulty of 1-5: "))
    
    print(f"You have selected {game_select[user_game_select]} with Difficulty {user_difficulty_select}")
    return user_game_select, user_difficulty_select

def main_menu():
    user_name = welcome()
    while True:
        game, difficulty = start_play()
        user_wins = play(game, difficulty)
        if user_wins:
            add_score(difficulty)
        
        play_again = input("Do you want to play another game? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing! See you next time.")
            break

if __name__ == "__main__":
    main_menu()
# This file acts as the main menu and entry point for the games.

def welcome():
    user_name_input = input("Please Enter Your Username: ")
    print(f"Hi {user_name_input} and welcome to the World of Games: The Epic Journey")
    return user_name_input

def start_play():
    game_select = {
        "1": "Memory Game",
        "2": "Guess Game",
        "3": "Currency Roulette"
    }
    user_game_select = input("""Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
2. Guess Game - guess a number and see if you chose like the computer.
3. Currency Roulette - try and guess the value of a random amount of USD in ILS 
Your choice: """)
    
    while user_game_select not in game_select:
        print("Invalid selection. Please choose a valid game.")
        user_game_select = input("Please choose a game to play (1, 2, or 3): ")
    
    user_difficulty_select = input("Thank you for selecting the game, please select a difficulty of 1-5: ")
    
    while not user_difficulty_select.isdigit() or not (1 <= int(user_difficulty_select) <= 5):
        print("Invalid difficulty level. Please select a number between 1 and 5.")
        user_difficulty_select = input("Please select a difficulty of 1-5: ")
    
    print(f"You have selected {game_select[user_game_select]} with Difficulty {user_difficulty_select}")
    return user_game_select, user_difficulty_select

if __name__ == "__main__":
    user_name = welcome()
    game, difficulty = start_play()
    
    if game == "3":
        from currency_roulette_game import play_currency_roulette
        play_currency_roulette(difficulty)
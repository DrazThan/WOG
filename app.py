from score import add_score
from currency_roulette_game import play_currency_roulette
from memory_game import generate_sequence,get_list_from_user,is_list_equal
from guess_game import generate_number, get_guess_user, compare_results


# This file acts as the main menu and entry point for the games.
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
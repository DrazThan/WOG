from memory_game import generate_sequence, get_list_from_user, is_list_equal
from guess_game import generate_number, get_guess_user, compare_results
from currency_roulette_game import play_currency_roulette

def play(game, difficulty):
    if game == 1:
        random_list = generate_sequence(difficulty)
        user_list = get_list_from_user()    
        return is_list_equal(user_list, random_list)
    elif game == 2:
        random_number = generate_number(difficulty)
        user_guess = get_guess_user(difficulty)
        return compare_results(user_guess, random_number)
    elif game == 3:
        return play_currency_roulette(difficulty)
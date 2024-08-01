# currency_roulette_game.py
import random
from currency_converter import CurrencyConverter

def get_money_interval(amount, from_currency, to_currency):
    try:
        c = CurrencyConverter()        
        converted_amount = c.convert(amount, from_currency, to_currency)
        return converted_amount
    except Exception as e:
        print(f"An error occurred during currency conversion: {e}")
        print(f"Error type: {type(e)}")
        return None

def play_currency_roulette(difficulty_level):
    random_number = random.randint(1, 100)
    random_number_converted = get_money_interval(random_number, 'USD', 'ILS')
    
    if random_number_converted is None:
        print("Sorry, we couldn't perform the currency conversion. Please try again later.")
        return False

    allowed_difference = 10 - int(difficulty_level)
    print(f"The allowed difference is: {allowed_difference}")
    user_guess = input(f"Please convert the following amount from USD to ILS {random_number}: ")
    
    try:
        if abs(float(random_number_converted) - float(user_guess)) <= allowed_difference:
            print(f"Congratulations! Your guess is within the allowed difference. The exact conversion was {random_number_converted:.2f} ILS.")
            user_wins = True
        else:
            print(f"You failed. The correct conversion was {random_number_converted:.2f} ILS.")
            user_wins = False
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        user_wins = False
    
    return user_wins

if __name__ == "__main__":
    # Test the currency conversion
    print("Testing currency conversion...")
    test_result = get_money_interval(1, 'USD', 'ILS')
    print(f"Test result: {test_result}")
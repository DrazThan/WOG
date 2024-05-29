# This file contains the Currency Roulette game logic.

import requests
import random

def get_money_interval(amount, from_currency, to_currency):
    try:
        url = f'https://v6.exchangerate-api.com/v6/e2cce35ea4f3b261be89eb88/latest/USD'
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200:
            raise Exception("Error: API request unsuccessful.")
        
        if 'conversion_rates' not in data:
            raise Exception("Error: Conversion rates not found in the response.")
        
        if to_currency in data['conversion_rates']:
            rate = data['conversion_rates'][to_currency]
            converted_amount = amount * rate
            return converted_amount
        else:
            raise Exception(f"Error: Currency {to_currency} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Finished currency conversion.")

def play_currency_roulette(difficulty_level):
    random_number = random.randint(1,100)
    random_number_converted = get_money_interval(random_number, 'USD', 'ILS')
    allowed_difference = 10 - int(difficulty_level)
    print(f"The allowed difference is: {allowed_difference}")
    #print(f"Please conver the following ammount from USD to ILS {random_number_converted}")
    user_guess = input(f"Please convert the following ammount from USD to ILS {random_number_converted}: ")
    # Add the rest of your game logic here
    # if user_guess 
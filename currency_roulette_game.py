import requests
import random
from app import start_play, user_difficulty_select

def get_money_interval(amount, from_currency, to_currency):
    try:
        # Replace 'YOUR-API-KEY' with your actual API key from ExchangeRate-API
        url = f'https://v6.exchangerate-api.com/v6/e2cce35ea4f3b261be89eb88/latest/{from_currency}'
        
        # Making our request
        response = requests.get(url)
        data = response.json()
        
        # Check if the request was successful
        if response.status_code != 200:
            raise Exception("Error: API request unsuccessful.")
        
        # Check if the conversion rates are in the response data
        if 'conversion_rates' not in data:
            raise Exception("Error: Conversion rates not found in the response.")
        
        # Calculate the converted amount
        if to_currency in data['conversion_rates']:
            rate = data['conversion_rates'][to_currency]
            converted_amount = amount * rate
            return converted_amount
        else:
            raise Exception(f"Error: Currency {to_currency} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # This code will run whether an exception is caught or not
        print("hello")
        # Example usage

        user_difficulty_select = start_play()
        random_number = random.radint(1,100)
        random_number_converted = get_money_interval(random_number, 'USD', 'ILS')
        allowed_difference = 10 - int(user_difficulty_select)
        print(allowed_difference)
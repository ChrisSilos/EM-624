# Author -- Chris Silos
# EM 624

#Exercise 01

# This is a program that will mimic the conversion of an amount of US dollars into a currency of the user's choice

#The program prompts the user for the amount of USD they would like to exchange,
#   the currency they would like to exchange it for,
#   and the exchange rate between USD and their chosen currency

#The program is written as a loop (using while True) that will run until the user enters the appropriate values

while True:
    usd_to_convert = input('\nHow many US dollars would you like to exchange?: ') # Prompt the user for the amount of USD they would like to exchange

    if usd_to_convert.isdigit(): # Check if the input is a numeric value
        usd_to_convert = int(usd_to_convert) # Convert the input value to an integer

        exchange_currency = input('\nEnter the name of currency you are converting dollars to?: ') # Prompt user for the currency
        exchange_rate = input('\nWhat is the exchange rate? (number to multiply by): ') # Prompt the user for the exchange rate

        if exchange_rate.isdigit():
            exchange_rate = int(exchange_rate) # Convert the exchange rate to an integer
            exchanged_value = usd_to_convert * exchange_rate # Calculate the exchanged value
            print()
            print(f'You can exchange {usd_to_convert} USD for {exchanged_value} {exchange_currency}\n')
            break

        # Restart the loop if the input is not an integer
        else: 
            print('\nThe exchange rate must be an integer value (no letters or symbols). Please start over')
            continue
        
    # Restart the loop if the input is not an integer
    else:
        print('\nThe USD amount must be an integer (no letters or symbols). Please start over')
        continue

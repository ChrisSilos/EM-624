# Author -- Chris Silos
# EM 624

# Exercise 02

# This is a program that checks if a password inputted from the user is acceptable or not (based on the requirements outlined in the assignment)

# The program prompts the user to enter a password
# The password must meet these three requirements:
    # 1. Minimum length of 6 characters
    # 2. Maximum length of 10 characters
    # 3. Only include letters or numbers (no special characters)

# If the user enters an invalid password, the program shows which requirements they violated and re-prompts the user

#The program is written as a loop (using while True) that will run until the user enters a valid passoword or 'done' to quit


while True:
    password = input(
        '\nPlease enter your password, or enter "done" (without quotes) to quit: ')

    wrong_character = False  # Assume there are no invalid characters in the password
    too_long = False  # Assume the password is not too long
    too_short = False  # Assume the password is not too short

    if password == ('done'):  # Quit the program if the user enters 'done'
        print('\nGoodbye!\n')
        break

    else:
        # Create a list of acceptable characters in the password (any number or letter)
        acceptable_characters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E',
                                 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        for i in password:
            if i not in acceptable_characters:
                wrong_character = True  # Check if the user entered any invalid characters

        if len(password) > 10:
            too_long = True  # Check if the password is too long

        elif len(password) < 6:
            too_short = True  # Check if the password is too short

        if wrong_character or too_long or too_short:  # Check if any of the conditions are NOT met
            print('\nThere are errors in your password, including: ')

            if wrong_character:
                # Print the appropriate error for incorrect characters
                print(
                    'Invalid character (password must only contain letters and numbers)')
            if too_long:
                # Print the appropriate error for a password that is too long
                print('Above maximum length of 10 characters')
            if too_short:
                # Print the appropriate error for a password that is too short
                print('Below minimum length of 6 characters')

            print('Please try again!\n')
            # Return to the beginning of the loop (Re-prompt the user for their password)
            continue

        else:
            print('\nYour password has been accepted!\n')
            break

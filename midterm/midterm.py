# Author -- Chris Silos
# EM 624

# MIDTERM EXAM

# SECTION 2 - CODE CHECKING

# ---------- QUESTION 6 ----------
# Problem: The code repeats the word itself 4 times instead of each letter 4 times. Furthermore, the final output is a list instead of a string. 
# Correct version shown below

N = input("Enter your characters: ") # Prompt the user for an input
L = []
for letters in N:
    letters.split()
    L.append(letters*4) # Append each letter 4 times
newstring = ''.join(L) # Join the elements from the list into a string
print(newstring)

# ---------- QUESTION 7 ----------
# Problem: The code does not convert the input to a numeric value. There is also no counter to limit the print statement at the end of the code.
# Correct version shown below

while True:
    # Prompt the user to enter a number
    num = input('Enter a whole number:')

    # Check if the user wants to exit the program

    # Check if the input is a whole number
    if num.isdigit():
        original_num = int(num)
    else:
        # If the input is not a whole number, re-prompt the user
        print('Please try again')
        continue

    # Convert the original input to a floating point number + 1
    new_num = 1.00 * (original_num + 1)
    print(f'\nThe number entered plus 1 is: {new_num}')

    count = 0
    # Print the original number 'N' times. (ie. if the original input was '6', the print '6' 6 times)
    while count < original_num:
        print (original_num)
        count +=1
    break

# ---------- QUESTION 8 ----------
# Problem: The code returns "True" for every character regardless of whether it is a vowel or not. Furthermore, it does not filter out special characters ($, %, &, *, etc...)
# Correct version shown below

# List of vowels to check
vowels = ['a', 'e', 'i', 'o', 'u', 'y'] 

# List of acceptable characters to check
acceptable_characters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a',
                         's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

while True:
    # Prompt the user for an input and convert it to lowercase
    char = input(
        'Please enter an alphabetical character: ').lower() 
    
    # Exit the program if the user enters 'done'

    # Check if the input is a valid input (only alphabetical letters are acceptable)
    if char not in acceptable_characters:
        print('Invalid Input. Please try again.')
    else:
        # Check if the input is a vowel
        if char in vowels:
            print("True")
            break
        else:
            print("False")
            break


# ---------- Question 9 ----------
# Read the text file into a list
text_file = open('ai_trends.txt','r')
text_data = text_file.read()
text_words = text_data.split()
text_words_lowercase = []

# Append all the words into a new list in lowercase form (becuase the stopwords are all lowercase)
for i in text_words:
    text_words_lowercase.append(i.lower())

# Read the stopwords file into a lsit
stopwords_file = open('stopwords_en.txt','r')
stopwords_data = stopwords_file.read()
stopwords = stopwords_data.split()

# Create a list to hold the AI text without stopwords
text_without_stopwords = []
for i in text_words_lowercase:
    # Append the list item if it is NOT in the stopwords list
    if i not in stopwords:
        text_without_stopwords.append(i)
    else:
        continue

# Create an empty dictionary that holds the frequency of each word in the file
unique_words = dict() # <---------- ANSWER TO PART A
  
# Loop through each line of the file
for word in text_without_stopwords:
    
    # Check if the word is already in dictionary
    if word in unique_words:
        # Increment count of word by 1
        unique_words[word] = unique_words[word] + 1
    else:
        # Add the word to dictionary with count 1
        unique_words[word] = 1

total_characters = len(''.join(unique_words.keys())) # Calculate total number of characters from unique word list
total_words = len(unique_words.keys()) # Calculate total number of unique words
average_word_length = total_characters/total_words # <----------- ANSWER TO PART B
print(f'The average word length is {average_word_length}')

average_frequency = sum(unique_words.values())/len(unique_words.keys()) # <------------ ANSWER TO PART C
print(f'The average frequency is {average_frequency}')

# ANSWER TO PART D IS SHOWN BELOW
top_five = sorted(unique_words, key=unique_words.get, reverse=True)[:5] # Find the five words with the highest frequency
bottom_five = sorted(unique_words, key=unique_words.get, reverse=False)[:5] # Find the five words with the lowest frequency

print(f'The five words with the highest frequency are {top_five}')
print(f'The five words with the lowest frequency are {bottom_five}')

# Did not have time to complete part E :(



# ---------- QUESTION 10 ----------
import pandas as pd

df = pd.read_csv('cars.csv')

average_mileage = round(df['average-mileage'].mean(),2) # <---------- ANSWER TO PART A

# Create a dataframe with the values sorted by average mileage
ordered_by_mileage = df.sort_values(by='average-mileage').reset_index() 

# The first two rows in the dataframe will be the lowest mileage
lowest_mileage = [ordered_by_mileage.loc[0], ordered_by_mileage.loc[1]] # <---------- ANSWER TO PART B

# The last two rows in the dataframe will be the highest mileage
highest_mileage = [ordered_by_mileage.loc[60], ordered_by_mileage.loc[59]] # <------------- ANSWER TO PART C

print(f'The average mileage is {average_mileage}')
print(f'\nThe lowest mileage models are shown below\n {lowest_mileage}')
print(f'\nThe highest mileage models are shown below\n {highest_mileage}')
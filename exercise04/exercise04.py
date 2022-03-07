# Author -- Chris Silos
# EM 624

# Exercise 04

# This is a program that processes two citi bike files and provides general information about each one

# The program outputs the following information for each file
# 1. The first and last date in the file
# 2. The average number of miles traveled
# 3. The total number of passes purchased
# 4. The three days with the highest and lowest number of trips (6 days in total)

# The program then combines the two files into a pandas dataframe and prints it


# Import libraries
import numpy as np
import pandas as pd

# Begin the txt part of the assignment
file = open('citi_bike.txt')  # Read the text file
text_data = []  # Define a list to hold the information from the text file

for line in file:  # Read each line in the file
    parts = line.strip().split()  # Strip the white space and create a list of items
    text_data.append(parts)  # Append that item's list to the data list

# Create a function to print specific information about the file
def print_details(data):

    # Create a list to hold the daily miles for each line
    daily_miles = [float(line[3]) for line in data]
    # Create a list to hold the daily pass purchases for each line
    pass_purchases = [int(line[7]) for line in data]
    # Create a list to hold the number of trips for each line
    trips = [int(line[1]) for line in data]
    # Create a list to hold the dates for each line
    dates = [line[0] for line in data]

    # Calculate the mean daily miles for the dataset
    average_daily_miles = np.array(daily_miles).mean()
    # Calculate the sum of the total passes for the dataset
    total_passes = np.array(pass_purchases).sum()

    # Order both the 'trips' and 'dates' lists by number of trips in ascending order to find the three highest and lowest days by number of trips
    for i in range(len(trips)):
        for j in range(i + 1, len(trips)):
            if(trips[i] > trips[j]):
                temp_trip = trips[i]
                temp_date = dates[i]

                trips[i] = trips[j]
                dates[i] = dates[j]

                trips[j] = temp_trip
                dates[j] = temp_date

    # Print the range of dates for the dataset
    print(f'\nThe following data is from {data[0][0]} to {data[-1][0]}')
    # Print the average daily miles
    print(f'\nAverage daily miles: {average_daily_miles:.2f} mi')
    # Print the total number of passes purchased
    print(f'\nTotal number of passes purchased: {total_passes} passes')
    print(f'\nThree days with highest number of trips: {dates[-3:]}')
    print(f'\nThree days with lowest number of trips: {dates [:3]}')


# Print the results for the txt file
print('\n----- PART ONE -----')
print_details(text_data)

# Begin the csv part of the assignment
file = open('citi_bike.csv')  # Read the csv file
csv_data = []  # Define a list to hold the information from the csv file

for line in file:  # Read each line in the file
    parts = line.strip().split(',')  # Strip the white space and create a list of items
    csv_data.append(parts)  # Append that item's list to the data list

# Print the results for the csv file
print('\n----- PART TWO -----')
print_details(csv_data)

print('\n----- PART THREE -----')
# Create list to hold column titles
headers = ['Date', 'Trips Over Last 24hrs', 'Cumulative Trips', 'Miles Traveled Today', 'Miles Traveled to Date',
           'Total Annual Members', 'Annual Member Sign-ups', '24hr Passes Purchased', '7 Day Passes Purchased']

# Create a dataframe for the text data
txt_df = pd.DataFrame(text_data, columns=headers)
# Create a dataframe for the csv data
csv_df = pd.DataFrame(csv_data, columns=headers)
# Concatenate the dataframes
final_df = pd.concat([csv_df, txt_df], ignore_index=True)

print()
# Print the merged dataframe
print(final_df)
print('\nThis is the end of the file processing')

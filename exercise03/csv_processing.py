# Author -- Chris Silos
# EM 624

# Exercise 03

# This is a program that processes two csv files and provides general information about each one

# The program first processes a csv file related to the January-February period and returns the following information:
    # 1. The last five lines in the file
    # 2. The number of lines in the file
    # 3. The number of lines in the file with usertype "Subscriber"
    # 4. The number of lines in the file with usertype "Customer"
    # 5. The percentage of lines with usertype "Customer"

# The program then processes a csv file related to the April-May period and returns the following information:
    # 1. The first five lines in the file
    # 2. The number of lines in the file
    # 3. The number of lines in the file with usertype "Subscriber"
    # 4. The number of lines in the file with usertype "Customer"
    # 5. Which of the two files is larger
    # 6. Which of the two files has a higher percentage of "Customer" usertype


# Begin processing the first file
table = [] # Create a list to hold each line in the file

# Create variables to count the numbers of lines, customers, and subscribers in the file
num_customers_janfeb = 0 
num_subscribers_janfeb = 0 
num_lines_janfeb = -1 # This is negative to account for the header (does not count as a line)

with open ('NYC-CitiBike-Jan_Feb2016.csv') as jan_feb: # Open the file
    line = jan_feb.readline()

    while line:
        line = line.split(',') # Convert each line into a list by splitting at commas (because it is a comma separated file)

        # The third to last value in each line determines if it is a customer or a subscriber

        if line[-3] == 'Customer': # If the value is 'Customer', increase the count of customers by one
            num_customers_janfeb += 1
        elif line[-3] == 'Subscriber': # If the value is 'Subscriber', increase the count of subscribers by one
            num_subscribers_janfeb += 1

        table.append(line) # Append each line to table
        num_lines_janfeb += 1 # Increase the count of lines by one
        line = jan_feb.readline() # Move onto the next line

    print('\nThese are the last five lines of the January-February file: \n')
    for line in table[-5:]:
        print(line)

    customer_pct_janfeb = round(num_customers_janfeb/num_lines_janfeb*100,2) # Calculate the percentage of customers

    # Print summary information for the file
    print(f'\nThe January-February file has {num_lines_janfeb} lines. Of those, {num_customers_janfeb} have usertype as "Customer", and {num_subscribers_janfeb} have usertype as "Subscriber". "Customer" is {customer_pct_janfeb}% of the total.')


# Begin processing the second file
table = [] # Create a list to hold each line in the file

# Create variables to count the numbers of lines, customers, and subscribers in the file
num_customers_apr_may = 0 
num_subscribers_apr_may = 0 
num_lines_apr_may = -1 # This value is negative to account for the header (does not count as a line)

with open ('NYC-CitiBike-Apr_May2016.csv') as apr_may: # Open the file
    line = apr_may.readline()

    while line:
        line = line.split(',') # Convert each line into a list by splitting at commas (because it is a comma separated file)

        # The third to last value in each line determines if it is a customer or a subscriber

        if line[-3] == 'Customer': # If the value is 'Customer', increase the count of customers by one
            num_customers_apr_may += 1
        elif line[-3] == 'Subscriber': # If the value is 'Subscriber', increase the count of subscribers by one
            num_subscribers_apr_may += 1

        table.append(line) # Append each line to table
        num_lines_apr_may += 1 # Increase the count of lines by one
        line = apr_may.readline() # Move onto the next line

    print('\nThese are the first five lines of the April-May file (not including column titles): \n')
    for line in table[1:6]:
        print(line)
    
    customer_pct_apr_may = round(num_customers_apr_may/num_lines_apr_may*100,2) # Calculate the percentage of customers

    # Print summary information for the file
    print(f'\nThe April-May file has {num_lines_apr_may} lines. Of those, {num_customers_apr_may} have usertype as "Customer", and {num_subscribers_apr_may} have usertype as "Subscriber".\n')

    if num_lines_janfeb > num_lines_apr_may:
        print('The first file is larger than the second one')
    else:
        print('The first file is smaller than the second one')

    if customer_pct_janfeb > customer_pct_apr_may:
        print('The first file has relatively more customers than the second one\n')
    else:
        print('The first file has relatively less customers than the second one\n')

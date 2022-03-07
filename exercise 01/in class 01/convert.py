# In class Excersize 01
# Sample progam

# This program converts celsius temperatures to fahrenheit

# The program is written as a loop (using while True), so that the user
#     must enter the word 'done" (without quotes) to signal
#     that they want to end


print('\nRun by Chris Silos\n')
while True:  
    temp_celsius = input("What is the temperature in Celsius you want to convert? (enter 'done' (no quotes) to stop the program): ")
    if temp_celsius == 'done':
        break
    else:
        temp_celsius = int(temp_celsius) # Convert input to integer
        temp_far = temp_celsius*(9/5) + 32 # Convert value to fahrenheit

        print (f'Your temperature is equivalent to {temp_far} degrees Fahrenheit')

print ('\nThanks for using this tool!\n')
# Author:  ---

# Exercise 00.2
# Sample progam

# This program read a txt file containing names
#    print the names and their frequencies and
#   the name with the highest frequency


# initializing the variable that will be used to hold the values to be printed
counter_dict = {}
num_max_freq = 0
name_max_freq = ''

# starting the loop on the lines of the input file
with open('names.txt') as in_file: # opening the file
	line = in_file.readline() # reading a line
	while line:
		line = line.strip()
		# strip() removes all whitespace at the start and end
		#  including spaces, tabs, newlines and carriage returns
		if line in counter_dict: # checking if the name is already in the dictionary
			counter_dict[line] += 1 # if yes, adding 1 to the counter
			if counter_dict[line] >= num_max_freq: # checking if current frequency is the max
			    num_max_freq = counter_dict[line]
			    name_max_freq = line
		else:
			counter_dict[line] = 1
		line = in_file.readline() # reading the next line

# printing the results
print ('\nThe following is the list of names in the file and their occurrences\n', counter_dict)
print ('\nThe name occourring the most is', name_max_freq, 'with', num_max_freq, 'occurrences')


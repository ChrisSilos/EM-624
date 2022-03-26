
#6
N = input("Enter your characters: ")
L = []
for letters in N:
    letters.split()
    L.append(letters)
print (L*4)

#7
while True:
	#prompts and receives user input
	char = input('Please enter an alphabetical character: ')

	if char.isdigit(): #checks if input is numerical
		print ('Invalid input.')
	else:
		if len(char) > 1: #checks if input is more than one character
			print ('Invalid input.')
		else:
			if char == 'a' or 'e' or 'i' or 'o' or 'u' or 'y': #checks if input is a vowel
				print ('True')
			else:
				print ('False')


#8
num = input('enter a whole number: ')
num = num + 1
print ('\nthe number entered plus 1 is:', num)
count = 1
while count < num:
	print (num)



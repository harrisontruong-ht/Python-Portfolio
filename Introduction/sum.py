# This program adds together a series of numbers input by the user

#prompts the user for how many numbers they want to add together
numValues = int(input("How many numbers do you want to add together?"))

# Initialize the total to zero
valueTotal = 0

# Loop to get the numbers and add them together
i = 0
while( i < numValues ):
    a = int(input("please enter valid whole Integer #" + str(i+1) + ": "))
    valueTotal += a
    i += 1

# Print the total
print("The sum of the two numbers is: " + str(valueTotal));

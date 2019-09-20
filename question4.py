# ### Problem 4:
# Ask the user to enter a number between -10 to -5. If their input is not between the two numbers ask them to do it again until they get it right. Afterward they print the correct number, print "Good job"

# ***** INPUT DATA MORE THAN ONCE!!!!!  *****
userInput = int(input("Enter a number between -10 to -5."))

for (userInput < -10 or userInput > -5):
    userInput = input("Try again. Enter a number between -10 to -5.")
print("Good job")

'''# Get user input for a number
num = int(input("Enter the number: "))
# Display the entered number
print("You entered: ", num)

# Check if the number is odd or even
if num % 2 == 0:
    print("The number is even")
else:
    print("The number", num, "is odd.")
'''

# Multiplication table of a number provided by the user
#  Get user input for a number 
'''
num = int(input("Enter the number: "))

print("==========================")
print("Multiplication table of", num)
#  Generate the multiplication table
for i in range (1, 13):
    print(num, "x", i, "=", num * i)'''



# Program that takes 3 num as input from user and prints the largest number
# input : 12, 25, 7
# output : 25
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Find the largest number
if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)
'''

# Write a Python program that counts the number of vowels (a, e, i, o, u) in a given string.
# Input: Hello World
# Output: The number of vowels in "Hello World" is 3.


# Get user input for a string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Get the input string from the user
s = input("Enter a string: ")

# Count the vowels and print the result
vowel_count = count_vowels(s)
print(f"The number of vowels in \"{s}\" is {vowel_count}.")


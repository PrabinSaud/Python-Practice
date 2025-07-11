#Write a Python program that takes a number from the user and prints the sum of its digits.
numbers = (input("Enter numbers: "))
digit_sum = 0
for digit in numbers:
    digit_sum+= int(digit)
print("The sum of digits are: ",digit_sum)
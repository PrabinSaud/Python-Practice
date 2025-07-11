'''Write a Python program that takes a string from the user and prints it in reverse without 
 using built-in reverse methods or slicing.'''

text = "prawin"
rev_text = ""
for char in text:
    rev_text = char + rev_text
print("Reverse text is: ",rev_text)
word = str(input("Enter the word: "))
vowels = "aeiou"
count = 0
for char in word:
    if char.lower() in vowels:
        count+=1
print("Total number of vowel are: ", count)

#Write a Python program that takes a sentence as input and prints how many times each word appears.
sentences = input("Enter a sentence: ")
words = sentences.lower().split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
for word, count in frequency.items():
    print(f"{word} : {count}")
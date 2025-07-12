# Mannualy reversed the text
text = input("Enter t text: ")
revtext = ""
for char in text:
    revtext = char + revtext
if text == revtext:
        print(f"{text} is palindrom")
else:
        print(f"{text} is not palindrom")

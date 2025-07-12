#Using slicing method
text = input("Enter t text: ")
revtext= text[::-1]
if text==revtext:
    print("Plaindrom")
else:
    print("Not palindrom")
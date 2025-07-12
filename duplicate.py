#Write a Python program that removes all duplicate elements from a list while preserving the order.

numbers=[1,3,2,4,5,3,2]
unique=[]
for num in numbers:
    if num not in unique:
        unique.append(num)
newnum=sorted(unique)
print("List with duplicates: ", numbers)
print("List after removing duplicates: ",newnum)

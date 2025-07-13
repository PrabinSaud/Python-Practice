# Write a Python program to print all prime numbers in list.
numbers = list(range(10, 20))
prime = []

for num in numbers:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime.append(num)

print("Prime numbers from the list:", prime)

   
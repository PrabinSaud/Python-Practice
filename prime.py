num=int(input("enter an number: "))
if num<2:
    print("It's Prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("Not Prime")
            break
    else:
        print("It's Prime")
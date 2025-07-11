def swap():
    a=int(input("Enter the value of a: "))
    b=int(input("Enter the value of b: "))
    print(f"value of a={a} and b={b} before swap")
    a,b=b,a
    print(f"value of a={a} and b= {b} after swap")
swap()
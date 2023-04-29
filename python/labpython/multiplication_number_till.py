number1 = int(input("Enter an integer: "))
for i in range(1,number1+1):
    x = i
    print("Multiplication table for", x, "is:")
    for j in range(1,11):
        print(x * j)
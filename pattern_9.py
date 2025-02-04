n = int(input("Enter an odd number for the diamond size: "))

for i in range(n//2 + 1):
    for k in range(n//2 - i):
        print(" ",end="")

    for j in range(2*i + 1):
        if j == 0 or j == 2*i:
            print("*", end="")
        else:
            print(" ",end="")
    print()

for i in range(n//2 - 1, -1, -1):
    for k in range(n//2 - i):
        print(" ",end="")
    
    for j in range(2*i + 1):
        if j == 0 or j == 2*i:
            print("*", end="")
        else:
            print(" ",end="")   
    print()
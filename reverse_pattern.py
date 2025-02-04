num = int(input("Enter a number="))

for i in range(1, num+1):
    for k in range(num-i):
        print(" ",end="")
    for j in range(i):
        print(i,end="")
    print()
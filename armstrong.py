num = int(input("Enter a number="))
count = 0 
check = 0
temp = num

while temp > 0:
    temp //= 10
    count += 1

temp = num

while num > 0:
    mod = num % 10
    check = mod ** count + check
    num //= 10

if temp == check:
    print(temp," is an armstrong number")
else:
    print(temp," is not an armstrong number")
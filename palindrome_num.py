num = int(input("Enter a number="))
revNum = 0
temp = num

while num > 0:
    mod = num % 10
    revNum = revNum * 10 + mod
    num //= 10

if temp == revNum:
    print(temp,"is a palindrome number")
else:
    print(temp," is not a palindrome number")
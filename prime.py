num = int(input("Enter a number="))
flag = 0

for i in range(2, num):
    if num % i == 0:
        flag = 1
        break

ans = f"{num} is a prime number" if flag == 0 else f"{num} is not a prime number"
print(ans) 
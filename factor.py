num = int(input("Enter a number="))
lst = []

for i in range(1, num+1):
    if num % i == 0:
        lst.append(i)

print(f"Factors of given number is:- {lst}")
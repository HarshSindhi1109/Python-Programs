num = int(input("Enter a number="))
lst = []

for i in range(2, num+1):
    flag = 0
    for j in range(2, (i//2) + 1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        lst.append(i)

print(f"Prime numbers between 1 and {num}:-")
print(lst)
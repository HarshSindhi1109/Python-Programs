rows = int(input("Enter number of rows="))
cols = int(input("Enter number of columns="))
matrix1 = []
matrix2 = []
result = []

print("Enter values for first matrix:-")
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(value)
    matrix1.append(row)

print("Enter values for second matrix:-")
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(value)
    matrix2.append(row)

for i in range(rows):
    row = []
    for j in range(cols):
        res = matrix1[i][j] + matrix2[i][j]
        row.append(res)
    result.append(row)

print("Additon of two matrix is:-")
for i in range(rows):
    for j in range(cols):
        print(result[i][j],end=" ")
    print()
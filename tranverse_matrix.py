print("Enter values for 3*3 matrix:-")
matrix = []

for i in range(3):
    row = []
    for j in range(3):
        value = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(value)
    matrix.append(row)

print("\nThe 3*3 Matrix is:-")
for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print()

print("\nTranverse of Matrix:-")
for i in range(3):
    for j in range(3):
        print(matrix[j][i],end=" ")
    print()


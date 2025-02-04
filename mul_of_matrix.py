import numpy as np # type: ignore

rows1 = int(input("Enter the number of rows of first matrix: "))
cols1 = int(input("Enter the number of columns of first matrix: "))
rows2 = int(input("Enter the number of rows of second matrix: "))
cols2 = int(input("Enter the number of columns of second matrix: "))

if cols1 != rows2:
    print("Matrix multiplication is not possible! Columns of first matrix must equal rows of second matrix.")
else:
    print("Enter values for the first matrix row by row:")
    matrix1 = np.array([list(map(int, input(f"Row {i+1}: ").split())) for i in range(rows1)])

    print("Enter values for the second matrix row by row:")
    matrix2 = np.array([list(map(int, input(f"Row {i+1}: ").split())) for i in range(rows2)])

    result = np.dot(matrix1, matrix2)

    print("Output Matrix is:")
    for i in range(rows1):  
        for j in range(cols2):  
            print(result[i][j], end=" ")
        print()

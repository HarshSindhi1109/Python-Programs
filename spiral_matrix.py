def generate_spiral_matrix(matrix, rows, cols):
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    result = []

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        
    return result

rows = int(input("Enter number of rows="))
cols = int(input("Enter number of columns="))
matrix = []

print("Enter values for the matrix:-")
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(value)
    matrix.append(row)

spiral_matrix = generate_spiral_matrix(matrix, rows, cols)

print("Spiral Matrix:- ",spiral_matrix)

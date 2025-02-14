matrix = []
result = []

input_str = input("Enter data: ")

def matrix_to_string(matrix):
    matrix2 = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(matrix[j][i])
        matrix2.append(row)
        
    return ''.join([''.join(row) for row in matrix2])

if len(input_str) > 9 or len(input_str) == 0:
    print("Amount of data must be greater than zero and less than ten.")

else:
    index = 0
    for i in range(3):
        row = []
        for j in range(3):
            row.append(input_str[index] if index < len(input_str) else '')
            index += 1
        matrix.append(row)

    key = 213  # This is your key for encryption
    digits = [int(digit) for digit in str(key)]  # Convert the key into a list of digits

    # Ensure the key has exactly 3 digits (pad with leading zeroes if necessary)
    # while len(digits) < 3:
    #     digits.insert(0, 0)

    for i in range(3):
        row = []
        for j in range(3):
            # Use the digit as an index to select elements from the matrix
            # Fix: Ensure valid column index using modulo operation
            col_index = (digits[j] % 3) - 1
            res = matrix[i][col_index]  # Use digits[j] for column indexing
            row.append(res)
        result.append(row)

    print("Actual matrix is:-")
    for i in range(3):
        for j in range(3):
            print(matrix[i][j],end=" ")
        print()

    print("Encryption of the matrix is:-")
    for i in range(3):
        for j in range(3):
            print(result[i][j],end=" ")
        print()

    ans = matrix_to_string(result)
    print(ans)
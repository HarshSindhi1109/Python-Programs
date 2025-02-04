def reverse_array(arr):
    # Reversing the array using slicing
    return arr[::-1]

# Input from user
arr = list(map(int, input("Enter the elements of the array (separated by space): ").split()))

# Call the function and print the result
reversed_arr = reverse_array(arr)
print("Reversed array:", reversed_arr)

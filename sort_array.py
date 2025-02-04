def sort_array(arr):
    # Using the built-in sorted() function to sort the array
    return sorted(arr)

# Input from user
arr = list(map(int, input("Enter the elements of the array (separated by space): ").split()))

# Call the function and print the result
sorted_arr = sort_array(arr)
print("Sorted array:", sorted_arr)

def remove_duplicate(input_str):
    temp = []
    for char in input_str:
        if char not in temp:
            temp.append(char)
    # Return the stringified list as a string (not a list format)
    return ''.join(temp)

# Use a different variable name instead of `str`
input_str = input("Enter a string: ")
ans = remove_duplicate(input_str)
print(ans)

def remove_vowels(input_str):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in input_str if char not in vowels])

str = input("Enter a string:- ")
print(remove_vowels(str))

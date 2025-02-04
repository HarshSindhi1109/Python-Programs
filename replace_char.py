def replace_character(string, index, new_char):
    if index < 0 or index >= len(string):
        return "Invalid index"
    
    string_list = list(string)
    
    string_list[index] = new_char
    
    return ''.join(string_list)

string = input("Enter a string: ")
index = int(input("Enter the index to replace: "))
new_char = input("Enter the new character: ")

result = replace_character(string, index, new_char)
print("Updated string:", result)

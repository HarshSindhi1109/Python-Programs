def find_words(string, target):
    if target in string:
        return f"{target} is found in string."
    else:
        return f"{target} is not found in string."

string = input("Enter a string: ")
target = input("Enter the word you want to search in string: ")

result = find_words(string, target)
print(result)

def isCamelCase(input_str):
    if not input_str:
        return False
    
    if not input_str[0].islower():
        return False
    
    for i in range(1, len(input_str)):
        if input_str[i].isupper():
            if i + 1 < len(input_str) and not input_str[i+1].islower():
                return False
        elif not input_str[i].isalpha():
            return False
    
    if input_str[-1].isupper():
        return False
    
    return True 

input_str = input("Enter a string:- ")

if isCamelCase(input_str):
    print(input_str," is in camel case.")
else:
    print(input_str," is not in camel case.")
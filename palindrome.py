str = input("Enter a string:- ")

cleaned_str = str.replace(",", "").replace(" ", "").replace(".", "").lower()

import re
cleaned_str = re.sub(r'[^a-z0-9]','', cleaned_str)

if cleaned_str == cleaned_str[::-1]:
    print(str," is a palindrome string")
else:
    print(str," is not a palindrome string")
def swap_strings(s1, s2):
    s1, s2 = s2, s1
    return s1, s2

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

string1, string2 = swap_strings(string1, string2)
print("After swapping:")
print("First string:", string1)
print("Second string:", string2)

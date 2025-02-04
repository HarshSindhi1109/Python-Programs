def roman_to_integer(roman):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    } 
    total = 0
    length = len(roman)

    for i in range(length):
        current_value = roman_dict[roman[i]]

        if i + 1 < length and current_value < roman_dict[roman[i+1]]:
            total -= current_value
        else:
            total += current_value
    return total

roman_numeral = input("Enter a roman numeral: ")
result = roman_to_integer(roman_numeral)
print(f"The integer value of {roman_numeral} is {result}.")
    
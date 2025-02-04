from collections import Counter

def count_and_say(num):
    count = Counter(str(num))
    result = []

    for digit in sorted(count.keys(), key = lambda x: str(num).index(x)):
        result.append(f"{count[digit]} {digit}'s")
    
    return ", ".join(result)

num = int(input("Enter a number="))
print(count_and_say(num))
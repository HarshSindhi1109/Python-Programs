def remove_duplicates(lst):
    result = []
    seen = set()

    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

lst = list(map(int, input("Enter elements separated by space: ").split()))
print("List after removing duplicates:", remove_duplicates(lst))
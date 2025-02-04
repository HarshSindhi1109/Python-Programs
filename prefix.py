def longest_common_prefix(lst):
    if not lst:
        return ""
    
    prefix = lst[0]

    for i in range(1, len(lst)):
        while not lst[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

lst = list(input("Enter a list (separate with space):- ").split())
ans = longest_common_prefix(lst)
print(ans)
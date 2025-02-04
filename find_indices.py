def find_indices(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return None

arr = list(map(int, input("Enter elements of the array (space-separated): ").split()))
target = int(input("Enter target number="))

indices = find_indices(arr, target)

if indices:
    print(f"Indices: {indices}")
else:
    print("No pair found that adds up to the target sum.")
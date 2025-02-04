def permute(nums, path=[]):
    if not nums:
        print(path)
        return
    for i in range(len(nums)):
        permute(nums[:i]+nums[i+1:], path + [nums[i]])

num_lst = list(map(int, input("Enter numbers (separate with space):- ").split()))
permute(num_lst)
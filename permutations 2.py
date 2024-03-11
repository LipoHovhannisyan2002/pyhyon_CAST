def permuteUnique(self, nums):
    nums.sort()

    stack = [(nums, [])]
    res = []
    while stack:
        nums, path = stack.pop()
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            newNums = nums[:i] + nums[i+1:]
            newPath = path + [nums[i]]
            stack.append((newNums, newPath))
    return res

nums = [1,2,3]

print(permuteUnique(0,nums))

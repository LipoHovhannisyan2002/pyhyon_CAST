nums = [3, 3]
target = 6



def twoSum(nums, target):
    for i in range(len(nums)):

        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                output.append(i)
                output.append(j)
                return output


print(twoSum(nums, target))

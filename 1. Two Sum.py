def two_sum(nums, target):
    num_map = {}
    
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[num] = i
    
    return None

nums1 = [2, 7, 11, 15,5,48]
target1 = 9
print(two_sum(nums1, target1))

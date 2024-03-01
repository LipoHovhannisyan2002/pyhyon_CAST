from itertools import *
def permuteOnlyOne(nums):

    l = permutations(nums)
    visited =[]
    for i in l:
        if i not in visited:
            visited.append(i)

    return tuple(list(visited))

nums = [1,2,3]
print(permuteOnlyOne(nums))
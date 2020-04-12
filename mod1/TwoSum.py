# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def twoSum(nums: list[int], target: int) -> list[int]:
    temp=0
    length=len(nums)
    for i in range(len(nums)):
        temp=target-nums[i]
        if temp in nums[i:length]:
            ind=nums.index(temp)
            if i!=ind:
                break
    return([i,ind])
print(twoSum([1,2,3,4,5],7))
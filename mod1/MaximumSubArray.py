# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subt
# wrong at [-2,-1,-3]



from math import ceil
nums = [-2, -1, -3]
# nums = [-1, -2, -3]
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
length = len(nums)
start = 0
end = length
temp = 0
for i in range(length):
    # if nums[i] > 0:
    #     start = i
    # if nums[length-i-1] > 0:
    #     end = length-i-1
    sums = sum(nums[start:end])
    temp = sum(nums[i:end])
    temp2 = sum(nums[start:length-i])
    if sums < temp and start < end:
        start = i
    if temp2 > sums and start < end:
        end = length-i

print(sum(nums[start:end]))
print(nums[start:end])
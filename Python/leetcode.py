class Solution(object):
        nums = [3, 6, 7, 5]
        target = 12

def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            needed = target - nums[i]

        if needed in nums:
            print(needed)

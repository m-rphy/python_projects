# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            el = nums[i]
            comp = target - el
            if comp in dict:
                return dict[comp], i
            else:
                dict[el] = i
        return
    
nums = [-3,4,3,90]
solution = Solution()
print(solution.twoSum(nums, 0))
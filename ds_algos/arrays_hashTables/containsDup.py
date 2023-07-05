# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.
    
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dict = {}
    for el in nums:
        if el not in dict:
            dict[el] = el
        else: 
            return True
    return False


# PASSES

# nums = [1,2,3,4,5]

# print(containsDuplicate(nums))
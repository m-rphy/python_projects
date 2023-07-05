#  Q: Find the length of the longest subarray, 
#  with the same value in each position

def longestSubarray(nums):
    length = 0
    L = 0
    
    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R 
        length = max(length, R - L + 1)
    return length

#  How do you write the array above without L and R pointers

#  Q: Find the length subarray, where the sum is greater that or equal to the target.
#  Assume all the values are positive (Important note/ hint!!)

#  O(n) time complexity and O(1) space complexity

def shortestSubarry(nums, target):
    L, total = 0, 0
    length = float('inf')

    #  Move R pointer right
    for R in range(len(nums)): # EXPAND THE WINDOW
        #  wioth every step, add the elemenet to the total
        total += nums[R]
        #  IF the total is greater than OR equal to the target
        while total >= target: # SHRINK THE WINDOW
            #  possibly re-assign the length
            length = min(R - L + 1, length)
            #  decrement the total by L pointer elements
            #  until the total < target
            total -+ nums[L]
            L += 1
    #  return o if length i infinite else return length
    return 0 if length == float('inf') else length

# Q: Given a sorted input array, return the two indices of two elements which 
# sums up to the target value. Assume there's exactly one solution.

def targetSum(nums, target):
    L, curSum = 0, 0
    R = len(nums) - 1

    while R > L:
        curSum = nums[R] + nums[L]
        if curSum > target:
           R -= 1
        elif curSum < target:
            L += 1
        elif curSum == target:
            return [L, R]
    return -1 # Not needed since there is always a solution, but generalizes the code

nums = [-1,2,4,6,9,10,12]
target = 1

print(targetSum(nums, target))
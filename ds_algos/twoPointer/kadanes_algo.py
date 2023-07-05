#Find a non-empty subarray with the largest sum

#Kadane's Algorith is O(n)

#There is a sliding window that is non obvious


# def kadanes(nums):
#     maxSum = nums[0]
#     curSum = 0

#     for n in nums:
#         # Ensuring that our current sum is never negative
#         curSum = max(curSum, 0)
#         curSum += n
#         maxSum = max(maxSum, curSum)
#     return maxSum

def kadanes(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        curSum = max(curSum, 0) + n
        maxSum = max(maxSum, curSum)
    
    return maxSum

#How do you return the actual subarray?
#   You need to keep track of the indexes of the subarray


def slidingWindow(nums):
    maxSum = nums[0]
    curSum = 0

    #  Set the indexes
    maxL, maxR = 0, 0
    L = 0

    #  R will change and L will be reassigned
    for R in range(len(nums)):
        # The first line of the kadanes for loop
        #  We've found a window that sums to a negative number
        if curSum < 0:
            curSum = 0
            L = R
        
        #  The second line of kadanes for loops
        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L , R
    
    #  Return the subArray defined by maxL and maxR
    return nums[maxL:maxR]

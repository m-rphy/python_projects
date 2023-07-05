


# Prefix Sum -> Starting at the beginning.... ?

#  nums = [2, -1, 3, -3, 4] ( any prefex is [2], [2, -1], [2, -1, 3],...)
#  a post fix if the same but from the end

def prefixSum(nums):
    preSum = 0

    for el in nums:
        preSum += el
    return preSum

def postFix(nums):
    postSum = 0

    for el in reversed(nums):
        postSum += el
    return postSum

# Q Given an array of values, design a data structure that can query the sum
#  of a subarray of the values

class PrefixSum:

    def __init__(self, nums):
        self.prefix = [] #an array of totals prefixes
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
    
    def rangeSum(self, left, right): #Assuming range sum is called much more frequently
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0 # Edge case for L = 0
        return (preRight - preLeft)

    # This allows you to add to the PrefixSum class in O(1) time complexity
    def addElement(self, element):
        newLastElement = element + self.prefix[-1]
        self.prefix.append(newLastElement)




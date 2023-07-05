# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """ 
    dict = {}
    for el in nums:
        if el in dict:
            dict[el] += 1
        if el not in dict:
            dict[el] = 1
    
    resultArr = sorted(dict, key=dict.get, reverse=True)
    return resultArr[0:k]

print(topKFrequent([1,1,1,2,2,3,3,3,3,3], 2))


# Almost done, but just having trouble with syntax
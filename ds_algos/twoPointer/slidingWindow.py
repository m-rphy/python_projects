# Given an array, return true if there 
# are two elements within a window of size k that are equal

def closeDuplicates(nums, k):
    #  Initialize a HastSet and L pointer
    window = set()
    L = 0

    #  Iterate through the array
    for R in range(len(nums)):
        #  If the two points extend past the window
        if R - L + 1 > k:
            #  Remove the left element and resize the window
            window.remove(nums[L])
            L += 1
        #  If there is an element inside the HashSet
        if nums[R] in window:
            return True
        #  Else add the element to the hashSet
        window.add(nums[R])

    #  Once we get the end of the array, w/o returning True...
    return False
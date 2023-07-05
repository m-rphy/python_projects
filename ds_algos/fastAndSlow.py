# Q: find the middle of a linkedList

# fast point is shifted by 2 (always?)
# slow point is incremented by 1 (always?)

def middleOfList(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

#  O(n) space complexity 
# fn hasCycle(head):
#     visited = set()
#     while head is not null:
#         if head in visited:
#             return true
#         head = head.next
#     return false

#  O(1) space complexity 
#  what if the LL has a cycle in it?
def cycleDetection(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


#  Where does the cycle start?
def cycleStart(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    if not fast or not fast.next:
        return None
    
    slow2 = head
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next

    return slow

# Mathematical Proof of Floyd's Tortoise and Hare

# 1. Let the distance between the head node and the node at which the cycle starts be denoted by P

# 2. Let the length of the cycle be denoted by C

# 3. Let the distance from the node at which slow and fast 
# intersect to the node at which the cycle begins, be denoted by X

# Using this information, we can derive that the distance between the head node and the node at which fast and slow intersect is C − X

# We know that 2∗slow = fast. Using the information above, let's rewrite this equation in terms of the 
# C,X,P, we get the following.
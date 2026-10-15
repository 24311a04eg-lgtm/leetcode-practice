# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        curr = head
        
        # First pass: push all values onto stack
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        # Second pass: compare with stack
        curr = head
        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next
        
        return True









        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        curr = head
      
        while stack and curr != stack[-1] and curr.next != stack[-1]:
            node = stack.pop()
            node.next = curr.next
            curr.next = node
            curr = node.next
        
        if stack:
            curr.next = stack.pop()
            curr = curr.next
        
        curr.next = None




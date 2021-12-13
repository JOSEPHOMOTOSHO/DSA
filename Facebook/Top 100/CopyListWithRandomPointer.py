
# Time = 0(N)
# Space = 0(N)

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # Two Pass Algo
        
        oldToCopy = {None: None}
        
        cur = head
        # create a copy of all the nodes in the linkedlist and stor in hashmap
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
            
        # set the copy's next and random pointers and return head
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
            
        return oldToCopy[head]
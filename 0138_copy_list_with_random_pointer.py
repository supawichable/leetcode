'''
138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        newHead = Node(head.val, None, None)
        newCurr = newHead
        oldCurr = head
        visited = {oldCurr: newCurr}

        def getClonedNode(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            visited[node] = Node(node.val, None, None)
            return visited[node]

        while oldCurr:
            newCurr.next = getClonedNode(oldCurr.next)
            newCurr.random = getClonedNode(oldCurr.random)
            oldCurr = oldCurr.next
            newCurr = newCurr.next

        return newHead


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        oldCurr = head
        
        while oldCurr:
            newNode = Node(oldCurr.val, None, None)
            newNode.next = oldCurr.next
            oldCurr.next = newNode
            if newNode.next == None:
                break
            oldCurr = newNode.next

        oldCurr = head
        
        while oldCurr:
            newCurr = oldCurr.next
            if oldCurr.random:
                newCurr.random = oldCurr.random.next
            else:
                newCurr.random = None
            if not oldCurr.next.next:
                break
            oldCurr = oldCurr.next.next
        
        newCurr = head.next
        newHead = head.next

        while newCurr:
            if newCurr.next == None:
                break
            newCurr.next = newCurr.next.next
            newCurr = newCurr.next

        return newHead
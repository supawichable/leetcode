'''
23. Merge K Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
'''


from queue import PriorityQueue


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = PriorityQueue()
        head = tmp = ListNode(0)
        idx = 0
        record = dict()
        for lst in lists:
            if lst:
                q.put((lst.val, idx))
                record[idx] = lst
                idx += 1
        while not q.empty():
            val, new_idx = q.get()
            node = record[new_idx]
            tmp.next = node
            tmp = tmp.next
            if node.next:
                q.put((node.next.val, idx))
                record[idx] = node.next
                idx += 1
        return head.next

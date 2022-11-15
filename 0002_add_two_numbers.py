'''
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_val(l):
            curr_sum = 0
            count = 0
            while l:
                curr_sum += l.val * (10 ** count)
                count += 1
                l = l.next
            return curr_sum

        def make_list(num):
            root = ListNode(-1)
            curr = root
            if num == 0:
                return ListNode(0)
            while num:
                newNode = ListNode(num % 10)
                num //= 10
                curr.next = newNode
                curr = curr.next
            return root.next

        curr1, curr2 = l1, l2
        return make_list(get_val(curr1) + get_val(curr2))

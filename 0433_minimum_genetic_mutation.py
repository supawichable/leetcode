'''
433. Minimum Genetic Mutation
https://leetcode.com/problems/minimum-genetic-mutation/
'''


from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        queue = deque([(start, 0)])
        seen = set()
        
        while queue:
            seq, steps = queue.popleft() 
            if seq == end:
                return steps
            for c in range(8):
                for g in 'ACGT':
                    new_seq = seq[:c] + g + seq[c + 1:]
                    if new_seq in bank_set and new_seq not in seen:
                        seen.add(new_seq)
                        queue.append((new_seq, steps + 1))
        
        return -1
    
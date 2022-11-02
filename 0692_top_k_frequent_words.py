'''
692. Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/
'''

from collections import Counter
import heapq


# Wrapper

class Solution:
    
    @total_ordering
    class Wrapper:
        def __init__(self, val, word):
            self.val = val
            self.word = word

        def __lt__(self, other):
            if self.val == other.val:
                return other.word < self.word
            return self.val < other.val
            
        def __eq__(self, other):
            return self.val == other.val and self.word == other.word
            
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
        heapq.heapify(heap)
        for word, freq in counter.items():
            heapq.heappush(heap, self.Wrapper(freq, word))
            if len(heap) > k:
                heapq.heappop(heap)
        return [item.word for item in sorted(heap, reverse=True)]


# Built-in nsmallest

class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        return heapq.nsmallest(k, counter.keys(), key=lambda x: (-counter[x], x))
            
        
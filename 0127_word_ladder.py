'''
127. Word Ladder
https://leetcode.com/problems/word-ladder/
'''


from collections import defaultdict, deque


# BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = deque([(beginWord, 0)])
        seen = set([beginWord])
        maskMap = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                masked = word[:i] + '*' + word[i+1:]
                maskMap[masked].append(word)
        
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps + 1
            for i in range(len(beginWord)):
                masked = word[:i] + '*' + word[i+1:]
                for candidate in maskMap[masked]:
                    if candidate not in seen:
                        seen.add(candidate)
                        queue.append((candidate, steps+1))
        return 0


# Bidirectional BFS
class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue_begin = deque([(beginWord)])
        queue_end = deque([(endWord)])
        seen_begin = {beginWord: 1}
        seen_end = {endWord: 1}
        maskMap = defaultdict(list)
        
        if endWord not in wordList:
            return 0
        
        for word in wordList:
            for i in range(len(word)):
                masked = word[:i] + '*' + word[i+1:]
                maskMap[masked].append(word)
        
        def bfs(queue, seen_self, seen_other):
            queue_len = len(queue)
            for _ in range(queue_len):
                word = queue.popleft()
                for i in range(len(word)):
                    masked = word[:i] + '*' + word[i+1:]
                    for candidate in maskMap[masked]:
                        if candidate in seen_other:
                            return seen_other[candidate] + seen_self[word]
                        if candidate not in seen_self:
                            seen_self[candidate] = seen_self[word] + 1
                            queue.append((candidate))
        
        while queue_begin and queue_end:
            if len(queue_begin) <= len(queue_end):
                ans = bfs(queue_begin, seen_begin, seen_end)
            else:
                ans = bfs(queue_end, seen_end, seen_begin)
            if ans:
                return ans

        return 0

'''
2225. Find Players With Zero or One Losses
https://leetcode.com/problems/find-players-with-zero-or-one-losses/
'''


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans0, ans1 = set(), set()
        lost2 = set()
        
        for winner, loser in matches:
            if winner not in lost2 and winner not in ans1:
                ans0.add(winner)
            if loser in ans0:
                ans0.remove(loser)
                ans1.add(loser)
            elif loser in ans1:
                ans1.remove(loser)
                lost2.add(loser)
            elif loser not in lost2:
                ans1.add(loser)
        return [sorted(list(ans0)), sorted(list(ans1))]

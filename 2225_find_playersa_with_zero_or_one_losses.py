'''
2225. Find Players With Zero or One Losses
https://leetcode.com/problems/find-players-with-zero-or-one-losses/
'''


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost0, lost1 = [], []
        lost_count = defaultdict(int)
        track_player = set()
        for match in matches:
            track_player.add(match[0])
            track_player.add(match[1])
            lost_count[match[1]] += 1
        for i in track_player:
            if i not in lost_count:
                lost0.append(i)
            elif lost_count[i] == 1:
                lost1.append(i)
        lost0.sort()
        lost1.sort()
        return [lost0, lost1]
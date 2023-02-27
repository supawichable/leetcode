'''
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
'''


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_t = Counter(t)
        if not cnt_t <= Counter(s):
            return ''
        shortest_len = float('inf')
        filtered_s = []
        for i, c in enumerate(s):
            if c in cnt_t:
                filtered_s.append((i, c))
        cnt_s = Counter()
        cnt_s[filtered_s[0][1]] += 1
        start, end = 0, 0
        res_start, res_end = start, end
        while end < len(filtered_s):
            if cnt_t <= cnt_s:
                if filtered_s[end][0] - filtered_s[start][0] + 1 < shortest_len:
                    res_start, res_end = filtered_s[start][0], filtered_s[end][0]
                    shortest_len = res_end - res_start + 1
                cnt_s[filtered_s[start][1]] -= 1
                start += 1
            else:
                end += 1
                if end < len(filtered_s):
                    cnt_s[filtered_s[end][1]] += 1
        return s[res_start:res_end+1]
add
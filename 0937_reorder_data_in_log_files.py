'''
937. Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/
'''


class Solution1:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for i, log in enumerate(logs):
            log = log.split()
            if log[1].isnumeric():
                digits.append(i)
            else:
                letters.append(i)
        letters.sort(key = lambda x: (logs[x].split()[1:], logs[x].split()[0]))
        return [logs[x] for x in letters] + [logs[x] for x in digits]


class Solution2:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def make_sort_key(log):
            split = log.split(maxsplit = 1)
            return (1, ) if split[1][0].isnumeric() else (0, split[1], split[0])
        return sorted(logs, key = make_sort_key)

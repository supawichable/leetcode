'''
819. Most Common Word
https://leetcode.com/problems/most-common-word/
'''


from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[!?\',;.]', ' ', paragraph)
        split = Counter(paragraph.lower().split())
        for b in banned:
            del split[b]
        return split.most_common(1)[0][0]

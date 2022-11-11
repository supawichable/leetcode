'''
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/
'''


class Trie:

    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        children = self.children
        for c in word:
            if c not in children:
                children[c] = Trie()
            children = children[c].children
        children['eow'] = Trie()

    def search(self, word: str) -> bool:
        children = self.children
        for c in word:
            if c in children:
                children = children[c].children
            else:
                return False
        return True if 'eow' in children else False

    def startsWith(self, prefix: str) -> bool:
        children = self.children
        for c in prefix:
            if c in children:
                children = children[c].children
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
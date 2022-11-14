'''
2467. Most Profitable Path in a Tree
https://leetcode.com/problems/most-profitable-path-in-a-tree/
'''


from collections import defaultdict, deque


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:   
        class Node:
            def __init__(self, val, gate, parent, steps_from_zero):
                self.val = val
                self.gate = gate
                self.parent = parent
                self.steps_from_zero = steps_from_zero
                self.steps_from_bob = len(amount)
                self.children = set()

        # build a graph from input
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        seen = set([0])
        root = Node(val = 0, 
                    gate = amount[0], 
                    parent = None,
                    steps_from_zero = 0)
        
        # BFS to construct the tree
        queue = deque([root])
        level = 1
        while queue:
            curr_level_length = len(queue)
            for _ in range(curr_level_length):
                curr_node = queue.popleft()
                for i in graph[curr_node.val]:
                    if i not in seen:
                        seen.add(i)
                        new_node = Node(val = i, 
                                       gate = amount[i], 
                                       parent = curr_node,
                                       steps_from_zero = level)
                        if i == bob:
                            bob_node = new_node
                        curr_node.children.add(new_node)
                        queue.append(new_node)
            level += 1
        
        # iterate bob path and fill in steps_from_bob
        tmp_node = bob_node
        i = 0
        while tmp_node:
            tmp_node.steps_from_bob = i
            i += 1
            tmp_node = tmp_node.parent

        # DFS to find max net_income
        def dfs(curr_alice, net_income):
            nonlocal ans
            # Bob and Alice are in the same node
            if curr_alice.steps_from_zero == curr_alice.steps_from_bob:
                net_income += curr_alice.gate / 2
            # Alice reaches the node before Bob therefore gain/pay the gate fee
            elif curr_alice.steps_from_zero < curr_alice.steps_from_bob:
                net_income += curr_alice.gate
            # Alice reaches leaf node
            if len(curr_alice.children) == 0:
                ans = max(ans, net_income)
                return
            for child_node in curr_alice.children:
                dfs(child_node, net_income)
        ans = float('-inf')
        dfs(root, 0)
        return int(ans)

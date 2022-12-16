'''
232. Implement Queue Using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/
'''


class MyQueue:

    def __init__(self):
        self.stack = []
        self.idx = 0

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.idx += 1
        return self.stack[self.idx - 1]

    def peek(self) -> int:
        return self.stack[self.idx]

    def empty(self) -> bool:
        return self.idx == len(self.stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

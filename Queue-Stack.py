from collections import deque

class Stack:
    def __init__(self):
        self.data = []

    def push(self, node):  # O(1)
        self.data.append(node)
    def pop(self): # O(1)
        self.data.pop()

class Queue:
    def __init__(self) -> None:
        self.data = []

    def enqueue(self,node):
        self.data.append(node)
    def dequeue(self):
        self.data = deque()
        
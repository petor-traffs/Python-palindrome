import sys

class Solution:

    def __init__(self):
        self.stack = []
        self.queue = []
    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def popCharacter(self):
        temporalVariable = self.stack.pop()
        return temporalVariable

    def dequeueCharacter(self):
        temporalVariable2 = self.queue.pop(0)
        return temporalVariable2





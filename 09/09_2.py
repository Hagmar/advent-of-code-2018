import sys
from collections import defaultdict

class LinkedList:
    class Node:
        def __init__(self, v, p=None, n=None):
            self.v = v
            self.p = p
            self.n = n

        def __repr__(self):
            return 'Node({})'.format(self.v)

    def __init__(self):
        self.initial = self.Node(0)
        self.initial.n = self.initial
        self.initial.p = self.initial
        self.size = 0

    def __repr__(self):
        x = [self.initial.v]
        curr = self.initial.n
        while curr != self.initial:
            x.append(curr.v)
            curr = curr.n
        return str(x)

    def __len__(self):
        return self.size

    def remove(self, n):
        n.p.n = n.n
        n.n.p = n.p
        self.size -= 1
        return n.n

    def add_after(self, n, new_v):
        new_n = self.Node(new_v, n, n.n)
        n.n.p = new_n
        n.n = new_n
        return new_n

players = 412
last = 71646 * 100

circle = LinkedList()
player = 0
scores = defaultdict(int)
current = circle.initial

for marble in range(1, last+1):
    if not marble % 23:
        for _ in range(7):
            current = current.p
        scores[player] += marble + current.v
        current = circle.remove(current)
    else:
        current = circle.add_after(current.n, marble)
    player = (player + 1) % players
print(max(scores.values()))

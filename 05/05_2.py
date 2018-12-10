import sys
import string

class LinkedList:
    class Node:
        def __init__(self, v, p=None, n=None):
            self.v = v
            self.p = p
            self.n = n

    def __init__(self, xs):
        self.size = len(xs)
        last = self.Node(None, None)
        self.initial = last
        for i in range(len(xs)):
            n = self.Node(i, last)
            if last:
                last.n = n
            last = n

    def __len__(self):
        return self.size

    def remove(self, n):
        n.p.n = n.n
        n.n.p = n.p
        self.size -= 1

line = sys.stdin.read().strip()
best_c = 'a'
best = len(line)

for c in string.ascii_lowercase:
    line2 = [x for x in line if x != c and x != c.upper()]
    llist = LinkedList(range(len(line2)))
    while True:
        done = True
        i = llist.initial.n
        while i.n.n:
            if line2[i.v].upper() == line2[i.n.v].upper() and line2[i.v] != line2[i.n.v]:
                llist.remove(i)
                llist.remove(i.n)
                i = i.p if i.p.v else i.n.n
                done = False
            else:
                i = i.n
        if done:
            break
    if len(llist) < best:
        best = len(llist)
        best_c = c
print(best_c)
print(best)

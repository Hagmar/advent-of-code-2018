import sys
from collections import defaultdict

lines = [line.strip() for line in sys.stdin.readlines()]

deps = defaultdict(set)
todo = set()
for line in lines:
    _, first, _, _, _, _, _, second, _, _ = line.split()
    deps[second].add(first)
    todo.add(first)
    todo.add(second)

order = []
while todo:
    for step in sorted(todo):
        if not deps[step].intersection(todo):
            todo.remove(step)
            order.append(step)
            break

print(''.join(order))

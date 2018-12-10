import sys
from collections import defaultdict
from string import ascii_uppercase

lines = [line.strip() for line in sys.stdin.readlines()]

deps = defaultdict(set)
todo = set()
for line in lines:
    _, first, _, _, _, _, _, second, _, _ = line.split()
    deps[second].add(first)
    todo.add(first)
    todo.add(second)

available = sorted(x for x in todo if not deps[x])

workers = [(None, 0)] * 5
time = 0
in_progress = set()
while todo:
    step_i = 0
    for step_i in range(len(available)):
        for i, worker in enumerate(workers):
            if not worker[0]:
                step = available.pop(0)
                workers[i] = (step, time + 60 + ascii_uppercase.index(step) + 1)
                step_i -= 1
                in_progress.add(step)
                break
        step_i += 1
    time = min(filter(lambda w: w[0], workers), key=lambda w: w[1])[1]

    for i, worker in enumerate(workers):
        if worker[1] <= time:
            step = worker[0]
            if step:
                todo.remove(step)
                in_progress.remove(step)
                workers[i] = (None, 0)

    for step in sorted(todo):
        if step not in available and step not in in_progress:
            if not deps[step].intersection(todo):
                available.append(step)

print(time)

import sys
from collections import defaultdict, deque

initial = list(input().strip().split()[2])
input()
lines = sys.stdin.readlines()

mappings = defaultdict(lambda: '.')
for line in lines:
    pattern = tuple(line.strip().split()[0])
    mappings[pattern] = '#'

print(mappings)

print(''.join(initial))
state = initial
first = 0
for x in range(20):
    next_state = []
    part = deque(initial[:4], 5)
    part = deque('....', 5)

    i = 0
    while state[i] == '.':
        part.append(state[i])
        i += 1

    first_set = False
    new_first = 0
    for i in range(i, len(state)+4):
        if i < len(state):
            part.append(state[i])
            if not first_set and state[i] == '#':
                new_first = first + i - 2
                first_set = True
        else:
            part.append('.')

        next_state.append(mappings[tuple(part)])

        # print('Part : ' + ''.join(part) + ' - ' + mappings[tuple(part)])
        # print(''.join(next_state))
    state = next_state
    first = new_first

    print(''.join(state) + ' first: ' + str(first))

print()
print(''.join(initial))
print(''.join(state))

total = 0
for i, c in zip(range(first, len(state)), state):
    if c == '#':
        total += i


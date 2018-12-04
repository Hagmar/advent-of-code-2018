import sys
from collections import defaultdict

lines = sys.stdin.readlines()

fabric = defaultdict(int)
claims = defaultdict(set)
claim_free = defaultdict(bool)

for line in lines:
    claim, _, coords, size = line.strip().split()
    x, y = map(int, coords[:-1].split(','))
    x_size, y_size = map(int, size.split('x'))
    claim = claim[1:]
    claim_free[claim] = True

    for x_curr in range(x, x + x_size):
        for y_curr in range(y, y + y_size):
            fabric[(y_curr, x_curr)] += 1
            claims[(y_curr, x_curr)].add(claim)
            if fabric[(y_curr, x_curr)] > 1:
                for k in claims[(y_curr, x_curr)]:
                    claim_free[k] = False

print([x[0] for x in claim_free.items() if x[1]][0])

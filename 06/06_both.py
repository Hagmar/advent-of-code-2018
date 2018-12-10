import sys
from collections import defaultdict

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

lines = sys.stdin.readlines()
max_x, max_y = 0, 0
starts=[]

for i, line in enumerate(lines):
    line = line.strip()
    x, y = map(int, line.split(', '))
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    starts.append((x,y))

inf = set()
sizes = defaultdict(int)
for x in range(max_x+1):
    for y in range(max_y+1):
        distances = sorted([(dist(p, (x,y)), i) for (i, p) in enumerate(starts)])
        if distances[0][0] != distances[1][0]:
            point_id = distances[0][1]
            sizes[point_id] += 1
            if not x or not y or x == max_x or y == max_y:
                inf.add(distances[0][1])
print(max([x[1] for x in sizes.items() if x[0] not in inf]))

tot = 0
for x in range(max_x+1):
    for y in range(max_y+1):
        distance = sum([dist(p, (x,y)) for p in starts])
        if distance < 10000:
            tot += 1
print(tot)

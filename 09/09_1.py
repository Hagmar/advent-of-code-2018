import sys
from collections import defaultdict

players = 412
last = 71646

circle = [0]
i = 0
player = 0
scores = defaultdict(int)

for marble in range(1, last+1):
    if not marble % 23:
        i_next = (i - 7) % len(circle)
        scores[player] += marble + circle[i_next]
        circle = circle[:i_next] + circle[i_next + 1:]
        i_next = i_next % len(circle)
    else:
        i_next = (i + 1) % (len(circle) + 0) + 1
        circle = circle[:i_next] + [marble] + circle[i_next:]
    player = (player + 1) % players
    i = i_next
print(max(scores.values()))

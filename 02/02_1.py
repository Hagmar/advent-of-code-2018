import sys
from collections import Counter

two = 0
three = 0
for line in sys.stdin.readlines():
    c = Counter(line)
    counts = set(c.values())
    if 2 in counts:
        two += 1
    if 3 in counts:
        three += 1
print(two*three)

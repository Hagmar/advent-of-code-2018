import sys
from collections import Counter

lines = sys.stdin.readlines()

two = 0
three = 0
for line in lines:
    c = Counter(line)
    ptwo = False
    pthree = False
    for k,v in c.items():
        if v == 2:
            ptwo = True
        if v == 3:
            pthree = True
    if ptwo:
        two += 1
    if pthree:
        three += 1
print(two*three)

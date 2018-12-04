import sys
from collections import defaultdict

lines = sys.stdin.readlines()
sleeps = defaultdict(lambda: defaultdict(int))
total_sleep = defaultdict(int)

guard = None
curr_hour = 0
curr_minute = 0
for line in lines:
    _, time, *rest = line.strip().split()
    hour = int(time[:2])
    minute = int(time[3:-1])

    if 'Guard' in rest:
        guard = int(rest[1][1:])
        curr_hour, curr_minute = 0, minute
    elif 'falls' in rest:
        curr_minute = minute
    elif 'wakes' in rest:
        s = sleeps[guard]
        for m in range(curr_minute, minute):
            s[m] += 1
        total_sleep[guard] += minute-curr_minute

rep_s = max(sleeps.items(), key=lambda x: max(x[1].values()))
rep_m = max(rep_s[1].items(), key=lambda x: x[1])[0]
print(rep_s[0] * rep_m)

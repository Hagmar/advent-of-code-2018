import sys

lines = sys.stdin.readlines()
for row, line in enumerate(lines):
    for line2 in lines[row+1:]:
        match = True
        diff_index = 0
        one_off = False
        for (i, (c1, c2)) in enumerate(zip(line, line2)):
            if c1 != c2:
                if not one_off:
                    one_off = True
                    diff_index = i
                else:
                    match = False
                    break
        if match:
            print(line[:diff_index-1] + line[diff_index:])

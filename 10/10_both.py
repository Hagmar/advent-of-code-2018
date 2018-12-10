import sys
import re

def draw(stars, time):
    min_y = min(x[1] for x in stars)
    max_y = max(x[1] for x in stars)
    if max_y - min_y > 10:
        return False

    min_x = min(x[0] for x in stars)
    max_x = max(x[0] for x in stars)

    star_pos = set()
    for star in stars:
        star_pos.add((star[0], star[1]))

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x,y) in star_pos:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print(time)
    return True

lines = sys.stdin.readlines()

stars = []
for line in lines:
    match = re.match(r'position=<([- \d]+), ([- \d]+)> velocity=<([- \d]+), ([- \d]+)>', line)
    x, y, x_v, y_v = map(int, match.groups())
    stars.append((x, y, x_v, y_v))

time = 0
while not draw(stars, time):
    for i, star in enumerate(stars):
        new_x = star[0] + star[2]
        new_y = star[1] + star[3]
        new_star = (new_x, new_y, star[2], star[3])
        stars[i] = new_star
    time += 1

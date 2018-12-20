from collections import defaultdict, Counter

def process_step(rooms, step, x_curr, y_curr):
    x_next, y_next = x_curr, y_curr
    if step == 'N':
        y_next -= 1
    elif step == 'S':
        y_next += 1
    elif step == 'E':
        x_next += 1
    elif step == 'W':
        x_next -= 1
    rooms[(x_curr, y_curr)].add((x_next, y_next))
    rooms[(x_next, y_next)].add((x_curr, y_curr))
    return x_next, y_next

def process(regex):
    piece = []
    root_piece = piece
    parents = []
    for i, c in enumerate(regex):
        if c == '(':
            parents.append(piece)
            new_piece = []
            piece.append(new_piece)
            parents.append(new_piece)
            piece = []
            new_piece.append(piece)
        elif c == ')':
            parents.pop()
            piece = parents.pop()
        elif c == '|':
            parent = parents[-1]
            piece = []
            parent.append(piece)
        else:
            piece.append(c)
    return root_piece

def traverse(tree, rooms, x_curr, y_curr, i):
    while i < len(tree):
        if type(tree[i]) == str:
            x_curr, y_curr = process_step(rooms, tree[i], x_curr, y_curr)
            i += 1
        else:
            for path in tree[i]:
                if path and all(map(lambda p: type(p) == str, path)):
                    count = Counter(path)
                    if (('N' not in count and 'S' not in count) or (count['N'] == count['S'])
                            and ('E' not in count and 'W' not in count) or (count['E'] == count['W'])):
                        for _ in traverse(path, rooms, x_curr, y_curr, 0):
                            pass
                        continue
                for x, y in traverse(path, rooms, x_curr, y_curr, 0):
                    for result in traverse(tree, rooms, x, y, i+1):
                        yield result
            return
    yield x_curr, y_curr

def find_max_distance(rooms):
    visited = set()
    next_rooms = {(0,0)}
    distance = 0
    over_1k = 0
    while rooms:
        next_step = set()
        for room in next_rooms:
            next_step.update(rooms[room])
            del rooms[room]
            visited.add(room)
        next_rooms = next_step.difference(visited)
        if distance >= 999:
            over_1k += len(next_rooms)
        if not next_rooms:
            return distance, over_1k
        distance += 1


regex = input()
tree = process(regex[1:-1])
rooms = defaultdict(set)
for _ in traverse(tree, rooms, 0, 0, 0):
    pass

print(find_max_distance(rooms))

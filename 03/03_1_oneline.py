print(sum(1 for x in __import__('collections').Counter((x,y) for l in map(lambda l:tuple(map(int,__import__('re').match(r'.*?(\d+),(\d+): (\d+)x(\d+)',l).groups())),__import__('sys').stdin.readlines()) for x in range(l[0],l[0]+l[2]) for y in range(l[1],l[1]+l[3])).values() if x>1))
__import__('functools').reduce(lambda s,x: (s[0]+x, s[1].union({s[0]})) if s[0] not in s[1] else exec("print(s[0]); __import__('sys').exit()"), __import__('itertools').cycle(map(int, __import__('sys').stdin.readlines())), (0, set()))
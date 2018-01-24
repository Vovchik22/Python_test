"""def unique (itter, seen = None):
    seen = set(seen or [])
    acc = []
    for i in itter:
        if i not in seen:
            seen.add(i)
            acc.append(i)
    return acc

xs = [1,1,2,3, 3, 4 ,4 ]
print(unique(xs))
"""
"""def unique (itter, seen = set()):
    acc = []
    for i in itter:
        if i not in seen:
            seen.add(i)
            acc.append(i)
    return acc

xs = [1,1,2,3, 3, 4 ,4 ]
print(unique(xs))"""

"""def flatten(xs, depth = None):
    pass

print(flatten([1, [2], 3], depth = 1 ))"""

"""def make_min(*, lo, hi):
    def inner (first, *args):
           res = hi
           for arg in (first, ) + args:
               if arg < res and arg < res < hi:
                  res = args
           return max(res, lo)
    return inner

b_m = make_min(lo = 0, hi = 255)
print (b_m(-5, 12, 13))"""

# euller 15

"""import math

def path (grid):
    p = math.factorial(grid *2) / (math.factorial(grid) ** 2)
    return p

n = path(2)
print(int(n))"""

import itertools
solution = []
count = 0

def path (grid):
    paths = []
    count = 0
    for i in range (0, grid):
        paths.append(0)
        paths.append(1)

    print (paths)

    for i in itertools.permutations(paths, grid * 2):
        if i not in solution:
            print (i)
            solution.append(i)
            count = count +1
    return count

print(path(20))

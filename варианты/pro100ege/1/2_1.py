import itertools

def f(x, y, z, w):
    return ((not x and y) == z) and w

for a in itertools.product([0,1], repeat=10):
    table = [(a[0], 0, a[1], a[2]), (a[3], a[4], a[5], 0), (0, 0, a[6], a[7]), (0, 0, a[8], a[9])]
    for p in itertools.permutations("xyzw"):
        if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1, 1] and len(set(table)) == 4:
            print("".join(p))

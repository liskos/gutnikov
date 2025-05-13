import math, turtle


def clasterization(data, r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if math.dist(p1, p2) <= r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters


def anticentroid(claster):
    r = []
    for p1 in claster:
        r.append((sum([math.dist(p1, p2) for p2 in claster]), p1))
    return max(r)[1]


r = open("27a.txt").readline()
r = float(r)
data = [list(map(float, line.split())) for line in open("27b.txt")][1:]
clasters = clasterization(data, r)
print([len(c) for c in clasters])
centrs = [anticentroid(c) for c in clasters]
print(centrs)
x, y = sum([p[0] for p in centrs]) / len(centrs), sum([p[1] for p in centrs]) / len(centrs)
print(x* 10000, y* 10000)

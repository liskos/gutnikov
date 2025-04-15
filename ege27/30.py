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


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red", "blue", "black"]
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x* 20,y* 20)
            turtle.dot(5, colors[i%len(colors)])
    turtle.done()


def centroid(claster):
    r = []
    for p1 in claster:
        r.append((sum([math.dist(p1, p2) for p2 in claster]), p1))
    return min(r)[1]


data = [list(map(float, line.split())) for line in open("27data/27-30a.txt")]
clasters = clasterization(data, 1)
clasters = [c for c in clasters if len(c) > 10]
print([len(c) for c in clasters])
visual(clasters)
centrs = [centroid(c) for c in clasters]
print(centrs)
x, y = sum([p[0] for p in centrs]) / len(centrs), sum([p[1] for p in centrs]) / len(centrs)
print(x* 100000, y* 100000)
print("---------------------------------------")
data = [list(map(float, line.split())) for line in open("27data/27-30b.txt")]
clasters = clasterization(data, 0.8)
clasters = [c for c in clasters if len(c) > 10]
print([len(c) for c in clasters])
centrs = [centroid(c) for c in clasters]
print(centrs)
x, y = sum([p[0] for p in centrs]) / len(centrs), sum([p[1] for p in centrs]) / len(centrs)
print(x* 100000, y* 100000)
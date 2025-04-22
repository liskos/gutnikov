import math, turtle


def clasterization1(data):
    clasters = [[],[],[]]
    for x,y in data:
        if x < 5:
            clasters[0].append([x,y])
        elif y > 5:
            clasters[1].append([x,y])
        elif y < 5:
            clasters[2].append([x,y])
    return clasters
def clasterization2(data):
    clasters = [[],[],[],[],[]]
    for x,y in data:
        if x > 10 and y < 10:
            clasters[0].append([x,y])
        elif y > x and x > 10:
            clasters[1].append([x,y])
        elif x > 10:
            clasters[2].append([x,y])
        elif y > x and x < 10:
            clasters[3].append([x,y])
        elif x < 10:
            clasters[4].append([x,y])
    return clasters
def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red", "blue", "orange", "green", "black"]
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x* 20,y* 20)
            turtle.dot(3, colors[i%len(colors)])
    turtle.done()

def centroid(claster):
    r = []
    for p1 in claster:
        r.append((sum([math.dist(p1, p2) for p2 in claster]), p1))
    return min(r)[1]

data = [list(map(float, line.split())) for line in open("27data/27-63a.txt")]
clasters = clasterization1(data)
print([len(c) for c in clasters])
visual(clasters)
centrs = [centroid(c) for c in clasters]
x, y = sum([x for x, y in centrs]) / len(centrs), sum([y for x, y in centrs]) / len(centrs)
print(x * 100000, y * 100000)
data = [list(map(float, line.split())) for line in open("27data/27-63b.txt")]
clasters = clasterization2(data)
print([len(c) for c in clasters])
centrs = [centroid(c) for c in clasters]
x, y = sum([x for x, y in centrs]) / len(centrs), sum([y for x, y in centrs]) / len(centrs)
print(x * 100000, y * 100000)

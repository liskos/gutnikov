import math, turtle


def clasterization_1(data):
    clasters = [[],[],[]]
    for x, y in data:
        if y < 0:
            clasters[0].append([x, y])
        elif y > 15:
            clasters[1].append([x, y])
        else:
            clasters[2].append([x, y])
    return clasters

def clasterization_2(data):
    clasters = [[],[],[]]
    for x, y in data:
        if x < 0:
            clasters[0].append([x, y])
        elif x > 15:
            clasters[1].append([x, y])
        else:
            clasters[2].append([x, y])
    return clasters


def visual1(clasters):
    turtle.tracer(0)
    turtle.up()
    color = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff"]
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x*10, y*10)
            turtle.dot(3, color[i])
    turtle.update()
    turtle.done()

def visual2(clasters, centers):
    turtle.tracer(0)
    turtle.up()
    color = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff"]
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x*10, y*10)
            turtle.dot(3, color[i])
    for x, y in centrs:
        turtle.goto(x*10, y*10)
        turtle.dot(6, "black")
    turtle.update()
    turtle.done()

def anticentroid(claster):
    s = 0
    p = [0, 0]
    for p1 in claster:
        d = sum([math.dist(p1, p2) for p2 in claster])
        if d > s:
            s = d
            p = p1
    return p

def retransl(data, centrs):
    p_best = [0,0]
    d_best = 0
    for p in data:
        d = sum(math.dist(p, c) for c in centrs)
        if d > d_best:
            d_best = d
            p_best = p
    return p_best


data = [list(map(float, line.split())) for line in open("27a.txt")]
clasters = clasterization_1(data.copy())
#visual1(clasters)
centrs = [anticentroid(c) for c in clasters]
#visual2(clasters, centrs)
x, y = retransl(data, centrs)
print(x* 10000, y* 10000)

data = [list(map(float, line.split())) for line in open("27b.txt")]
clasters = clasterization_2(data.copy())
visual1(clasters)
centrs = [anticentroid(c) for c in clasters]
#visual2(clasters, centrs)
x, y = retransl(data, centrs)
print(x* 10000, y* 10000)


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
def clasterization2(data):
    clasters = [[],[],[]]
    for x,y in data:
        if 1 <= x <= 6 and 1 <= y <= 5:
            clasters[0].append([x,y])
        elif 0 <= x <= 5 and 5 <= y <= 9:
            clasters[1].append([x,y])
        elif 7 <= x <= 11 and 2 <= y <= 7:
            clasters[2].append([x,y])
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
def minmax(claster1, claster2):
    mi1 = 10**10
    ma1 = 0
    for p1 in claster1:
        for p2 in claster2:
            s = math.dist(p1,p2)
            mi1 = min(s, mi1)
            ma1 = max(s, ma1)
    return mi1, ma1

# data = [list(map(float, line.split())) for line in open("27data/27-21a.txt")]
# clasters = clasterization(data, 1)
# clasters = [c for c in clasters if len(c) > 10]
# print([len(c) for c in clasters])
# for c in clasters:
#     w = max([x for x, y in c]) - min([x for x, y in c])
#     h = max([y for x, y in c]) - min([y for x, y in c])
#     print(f"H = {h}    W = {w}")
# visual(clasters)
# mi1, ma1 = minmax(clasters[0], clasters[1])
# print(mi1 * 10000, ma1 * 10000)

data = [list(map(float, line.split())) for line in open("27data/27-21b.txt")]
clasters = clasterization2(data)
print([len(c) for c in clasters])
for c in clasters:
    w = max([x for x, y in c]) - min([x for x, y in c])
    h = max([y for x, y in c]) - min([y for x, y in c])
    print(f"H = {h}    W = {w}")
visual(clasters)
mi1, ma1 = minmax(clasters[0], clasters[1])
mi2, ma2 = minmax(clasters[1], clasters[2])
mi3, ma3 = minmax(clasters[2], clasters[0])

print(min(mi1,mi2,mi3) * 10000, max(ma1,ma2,ma3) * 10000)
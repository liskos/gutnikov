import math, turtle

def clasterization(data, r):
    clasters = []
    while data:       # пока в дата есть точки
        clasters.append([data.pop()])  # начинаем новый кластре из одной точки из массива дата
        for p1 in clasters[-1]:# перебираем все звёзды последнего кластера
            sosedi = [p2 for p2 in data if math.dist(p1, p2) <= r] # находим соседей точки p1
            clasters[-1].extend(sosedi)# добавляем соседей в последний кластер
            for p in sosedi:
                data.remove(p)# удаляем соседей из дата
    return clasters



def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red", "black", "green", "pink", "orange"]
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x*20, y*20)
            turtle.dot(3,colors[i%len(colors)])
    turtle.done()

def centroid(claster):
    r = []
    for p1 in claster:
        r.append((sum([math.dist(p1, p2) for p2 in claster]), p1))
    return min(r)[1]
data = [list(map(float, line.split())) for line in open("27data/27-1a.txt")]
clasters = clasterization(data, 0.65)
print([len(c) for c in clasters])
#visual(clasters)
centrs = [centroid(c) for c in clasters]
print(centrs)
x, y = sum([p[0] for p in centrs]) / len(centrs), sum([p[1] for p in centrs]) / len(centrs)
print(x * 10000, y * 10000)
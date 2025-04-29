import math


file = open("27A(1).txt")
n, k = map(int, file.readline().split())
print(f"Плодородных {n}, Неплодородных {k}")
plod = [list(map(float, file.readline().split())) for _ in range(n)]
neplod = [list(map(float, file.readline().split())) for _ in range(k)]
razr = []
for p in plod:
    for p1 in neplod:
        if math.dist(p, p1) <= 5:
            break
    else:
        razr.append(p)
kol = []
for p in razr:
    s = sum([1 for p2 in razr if math.dist(p, p2) <= 7])
    kol.append([s, p])
kol.sort(key=lambda x:(x[0], sum(x[1])), reverse=True)
x, y = kol[0][1]
print(x*10**9, y*10**9)
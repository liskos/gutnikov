def f(x, y):
    return (x-2,y),(x,y-2),(x//3,y),(x,y//3)

a = [[" "] * 1500 for _ in range(1500)]

for i in range(1500):
    for j in range(1500):
        if i < 15 or j < 15:
            a[i][j] = "0"

for i in range(1500):
    for j in range(1500):
        if a[i][j] == " " and any(a[x][y] == "0" for x, y in f(i, j)):
            a[i][j] = "1"

for i in range(1500):
    for j in range(1500):
        if a[i][j] == " " and all(a[x][y] == "1" for x, y in f(i, j)):
            a[i][j] = "2"

for i in range(1500):
    for j in range(1500):
        if a[i][j] == " " and any(a[x][y] == "2" for x, y in f(i, j)):
            a[i][j] = "3"

for i in range(1500):
    for j in range(1500):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i, j)):
            a[i][j] = "4"
z = False
print([s for s in range(16,1500) if a[s][s] == "2"])
for s in reversed(range(16,1500)):
    for i, j in f(s, s):
        if [(i, j) for x, y in f(i, j) if a[x][y] == "1"]: # возм точки ваня ошибся
            print(s)
            z = True
            break
    if z: break
print([s for s in range(16,2000) if a[s][s] == "4"])
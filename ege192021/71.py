def f(x, y):
    return (x + 1,y), (x, y + 1), (x + y, y),(x,y + x)

a = [[" "] * 1000 for _ in range(1000)]

for i in range(1000):
    for j in range(1000):
        if i + j >= 68:
            a[i][j] = "0"

for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and any(a[x][y] == "0" for x, y in f(i, j)):
            a[i][j] = "1"

for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and all(a[x][y] == "1" for x, y in f(i, j)):
            a[i][j] = "2"

for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and any(a[x][y] == "2" for x, y in f(i, j)):
            a[i][j] = "3"

for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i, j)):
            a[i][j] = "4"

for s in range(1, 60):
    if any(a[x][y] == "1" for x, y in f(8, s)):
        print(s)
        break
print([s for s in range(1,60) if a[8][s] == "3"])
print([s for s in range(1,60) if a[8][s] == "4"])

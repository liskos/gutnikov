def f(x, y):
    return (x // 2, y), (x, y // 2), (x - 5, y + 2), (x + 2, y - 5)

a = [[" "] * 3000 for _ in range(3000)]

for i in range(3000):
    for j in range(3000):
        if i + j <= 69:
            a[i][j] = "0"

for i in range(3000):
    for j in range(3000):
        if a[i][j] == " " and any(a[x][y] == "0" for x, y in f(i, j)):
            a[i][j] = "1"

for i in range(3000):
    for j in range(3000):
        if a[i][j] == " " and all(a[x][y] == "1" for x, y in f(i, j)):
            a[i][j] = "2"

for i in range(3000):
    for j in range(3000):
        if a[i][j] == " " and any(a[x][y] == "2" for x, y in f(i, j)):
            a[i][j] = "3"

for i in range(3000):
    for j in range(3000):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i, j)):
            a[i][j] = "4"

print([s for s in range(51, 100) if a[35][s] == "2"])
print([s for s in range(51, 100) if a[35][s] == "3"])
print([s for s in range(51, 100) if a[35][s] == "4"])
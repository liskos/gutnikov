def f(x, y):
    return (x - 1, y),(x, y - 1),(x // 3, y),(x, y // 3)

a = [[" "] * 3000 for _ in range(3000)]

for i in range(3000):
    for j in range(3000):
        if i + j <= 63:
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

print([s for s in range(7,1000) if a[57][s] == "2"])
print([s for s in range(7,1000) if a[57][s] == "3"])
print([s for s in range(7,1000) if a[57][s] == "4"])

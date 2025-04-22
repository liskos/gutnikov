def f(x, y):
    return (x + 2, y), (x * 2, y), (x * 3, y), (x, y + 2), (x, y * 2), (x, y *3)

def fn(x, y):
    return (x + 2, y), (x * 2, y), (x, y + 2), (x, y * 2)

a = [[" "] * 1000 for _ in range(1000)]

for i in range(1000):
    for j in range(1000):
        if i + j >= 132:
            a[i][j] = "0"

for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and any(a[x][y] == "0" for x, y in fn(i, j)):
            a[i][j] = "1"

for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and all(a[x][y] == "1" for x, y in fn(i, j)):
            a[i][j] = "2"

for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and any(a[x][y] == "2" for x, y in f(i, j)):
            a[i][j] = "3"

for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i, j)):
            a[i][j] = "4"


print([s for s in range(1,101) if a[31][s] == "2"])
print([s for s in range(1,101) if a[31][s] == "3"])
print([s for s in range(1,101) if a[31][s] == "4"])
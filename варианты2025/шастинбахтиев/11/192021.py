def f(x, y):
    return (x + 3, y), (x * 2, y), (x, y + 3), (x, y * 2)

a = [[" "] * 400 for _ in range(400)]

for i in range(400):
    for j in range(400):
        if i + j >= 100:
            a[i][j] = "0"

for i in range(400):
    for j in range(400):
        if a[i][j] == " " and any(a[x][y] == "0" for x, y in f(i, j)):
            a[i][j] = "1"

for i in range(400):
    for j in range(400):
        if a[i][j] == " " and all(a[x][y] == "1" for x, y in f(i, j)):
            a[i][j] = "2"

for i in range(400):
    for j in range(400):
        if a[i][j] == " " and any(a[x][y] == "2" for x, y in f(i, j)):
            a[i][j] = "3"

for i in range(400):
    for j in range(400):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i, j)):
            a[i][j] = "4"

print([s for s in range(1, 82 + 1) if a[17][s] == "2"])
print([s for s in range(1, 82 + 1) if a[17][s] == "3"])
print([s for s in range(1, 82 + 1) if a[17][s] == "4"])

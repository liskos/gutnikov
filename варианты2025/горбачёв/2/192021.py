def f(x, y):
    return (x-2,y),(x,y-2),(x//3,y),(x,y//3)

a = [[" "] * 2000 for _ in range(2000)]

for i in range(2000):
    for j in range(2000):
        if i + j < 15:
            a[i][j] = "0"

for i in range(2000):
    for j in range(2000):
        if a[i][j] == " " and any(a[x][y] == "0" for x, y in f(i, j)):
            a[i][j] = "1"

for i in range(2000):
    for j in range(2000):
        if a[i][j] == " " and all(a[x][y] == "1" for x, y in f(i, j)):
            a[i][j] = "2"

for i in range(2000):
    for j in range(2000):
        if a[i][j] == " " and any(a[x][y] == "2" for x, y in f(i, j)):
            a[i][j] = "3"

for i in range(2000):
    for j in range(2000):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i, j)):
            a[i][j] = "4"

for s in range(16,2000):
    if any(a[x][y] == "1" for x,y in f(s, s)):
        print(s)
        break
print([s for s in range(16,2000) if a[s][s] == "3"])
print([s for s in range(16,2000) if a[s][s] == "4"])
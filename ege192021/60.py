def f(x,y):
    return (x+1,y),(x,y+1),(x*4,y),(x,y*4)

a = [[" "] * 1000 for _ in range(1000)]

for i in range(1000):
    for j in range(1000):
        if i + j >= 125:
            a[i][j] = "0"

for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and any(a[x][y] in "0" for x, y in f(i, j)):
            a[i][j] = "1"

for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and all(a[x][y] in "1" for x, y in f(i, j)):
            a[i][j] = "2"

for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and any(a[x][y] in "2" for x, y in f(i, j)):
            a[i][j] = "3"

for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i,j)):
            a[i][j] = "4"

for s in range(1, 118):
    if any(a[x][y] == "1" for x, y in f(7, s)):
        print(s)
        break
print([s for s in range(1, 118) if a[7][s] == "3"])
print([s for s in range(1, 118) if a[7][s] == "4"])
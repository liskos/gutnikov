def f(x,y):
    return (x-1,y),(x,y-1),(x//2,y),(x,y//2)

a = [[" "] * 2000 for _ in range(2000)]

for i in range(2000):
    for j in range(2000):
        if i + j <= 18:
            a[i][j] = "0"

for i in range(2000):
    for j in range(2000):
        if a[i][j] == " " and any(a[x][y] in "0" for x, y in f(i, j)):
            a[i][j] = "1"

for i in range(2000):
    for j in range(2000):
        if a[i][j] == " " and all(a[x][y] in "1" for x, y in f(i, j)):
            a[i][j] = "2"

for i in range(2000):
    for j in range(2000):
        if a[i][j] == " " and any(a[x][y] in "2" for x, y in f(i, j)):
            a[i][j] = "3"

for i in range(2000):
    for j in range(2000):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i,j)):
            a[i][j] = "4"


print([m for m in range(1, 100) if a[m][m] == "2"])
print([s for s in range(1,100) if a[13][s] == "3"])
print([m for m in range(1, 100) if a[m][m] == "4"])
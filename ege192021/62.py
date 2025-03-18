def f(x,y):
    return (x+1,y),(x,y+1),(x*2,y),(x,y*2)

a = [[" "] * 1000 for _ in range(1000)]

for i in range(1000):
    for j in range(1000):
        if i + j >= 30:
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

n=0
g=0
for k in range(1, 30):
    for s in range(1,30):
        if any(a[x][y] == "1" for x, y in f(k, s)):
            n+=1
print(n)

print([s for s in range(1, 30) if a[6][s] == "3"])
for k in range(1, 30):
    for s in range(1,30):
        if any(a[x][y] == "4" for x, y in f(k, s)):
            g += 1
print(g)
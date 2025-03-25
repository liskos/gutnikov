def f(x,y):
    return (x+1,y),(x,y+1),(x*2,y),(x,y*3)

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
        if k + s > 29:
            break
        else:
            if a[k][s] == "2":
                n+=1
print(n)

print([k for k in range(1, 30) if a[k][7] == "3"])
print([s for s in range(1, 30) if a[1][s]=="4"])

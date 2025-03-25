def f(x,y):
    return (x+2,y),(x,y+2),(x*3,y),(x,y*3)

a = [[" "] * 2000 for _ in range(2000)]

for i in range(2000):
    for j in range(2000):
        if i + j >= 45:
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

n=0
for k in range(1, 30):
    for s in range(1,30):
        if k + s > 43:
            break
        else:
            if a[k][s] == "2":
                n+=1
print(n)

print([s for s in range(1, 43) if a[4][s] == "3"])
print([s for s in range(1, 43) if a[13][s]=="4"])

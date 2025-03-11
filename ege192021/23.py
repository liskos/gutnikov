def f(x, y):
    return (x + 2,y),(x,y + 2),(x * 2,y),(x,y * 2)

a = [[" "] * 200 for _ in range(200)]

for i in range(200):
    for j in range(200):
        if i + j >= 73:
            a[i][j] = "0"

for i in range(200):
    for j in range(200):
        if a[i][j] == " " and any(a[x][y] in "0" for x, y in f(i,j)):
            a[i][j] = "1"

for i in range(200):
    for j in range(200):
        if a[i][j] == " " and all(a[x][y] in "1" for x, y in f(i,j)):
            a[i][j] = "2"

for i in range(200):
    for j in range(200):
        if a[i][j] == " " and any(a[x][y] in "2" for x, y in f(i,j)):
            a[i][j] = "3"

for i in range(200):
    for j in range(200):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i,j)):
            a[i][j] = "4"

for s in range(1,64):
    if any(a[x][y] == "1" for x,y in f(9, s)):
        print(s)
        break
print([s for s in range(1,64) if a[9][s] == "3"])
print([s for s in range(1,64) if a[9][s] == "4"])
def f(x, y):
    return (x + 1, y),(x,y + 1),(x * 2, y),(x, y * 2)


a = [[" "] * 175 for _ in range(175)]


for i in range(175):
    for j in range(175):
        if i + j >= 87:
            a[i][j] = "0"

for i in range(175):
    for j in range(175):
        if a[i][j] == " " and any(a[x][y] in "0" for x, y in f(i, j)):
            a[i][j] = "1"

for i in range(175):
    for j in range(175):
        if a[i][j] == " " and all(a[x][y] in "1" for x, y in f(i, j)):
            a[i][j] = "2"

for i in range(175):
    for j in range(175):
        if a[i][j] == " " and any(a[x][y] in "2" for x, y in f(i, j)):
            a[i][j] = "3"

for i in range(175):
    for j in range(175):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i, j)):
            a[i][j] = "4"


for s in range(1, 78):
    if any(a[x][y] == "1" for x, y in f(9, s)):
        print(s, sep="\t")
print("--------------")
print([s for s in range(1,78) if a[9][s] == "3"])
print([s for s in range(1,78) if a[9][s] == "4"])
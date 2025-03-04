def f(x, y):
    return (x-2,y),(x,y-2),((max(x,y)+1) // 2, min(x, y))


a = [[" "] * 500 for _ in range(500)]
for i in range(500):
    for j in range(500):
        if i + j <=33:
            a[i][j] = "0"


for i in range(500):
    for j in range(500):
        if a[i][j] == " " and any(a[x][y] == "0" for x, y in f(i, j)):
            a[i][j] = "1"


for i in range(500):
    for j in range(500):
        if a[i][j] == " " and all(a[x][y] == "1" for x, y in f(i, j)):
            a[i][j] = "2"


for i in range(500):
    for j in range(500):
        if a[i][j] == " " and any(a[x][y] == "2" for x, y in f(i, j)):
            a[i][j] = "3"


for i in range(500):
    for j in range(500):
        if a[i][j] == " " and all(a[x][y] in "13"  for x, y in f(i, j)):
            a[i][j] = "4"
# for i in range(1, 500):
#     print(*a[i][1:], sep="\t")
for s in range(11,500):
    if any(a[x][y] == "1" for x, y in f(23, s)):
            print(s, sep="\t")
print("-------------------")
print([s   for s in range(11,500) if a[23][s] == "3"])
print([s   for s in range(11,500) if a[23][s] == "4"])

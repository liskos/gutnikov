def f(x, y):
    return (x + 1, y),(x, y + 1),(x * 2, y),(x, y * 2)


a = [[" "] * 150 for _ in range(150)]

for i in range(150):
    for j in range(150):
        if i + j >= 75:
            a[i][j] = "0"
for i in range(150):
    for j in range(150):
        if a[i][j] == " " and any(a[x][y] in "0" for x, y in f(i, j)):
            a[i][j] = "1"
for i in range(150):
    for j in range(150):
        if a[i][j] == " " and all(a[x][y] in "1" for x, y in f(i, j)):
            a[i][j] = "2"
for i in range(150):
    for j in range(150):
        if a[i][j] == " " and any(a[x][y] in "2" for x, y in f(i, j)):
            a[i][j] = "3"
for i in range(150):
    for j in range(150):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i, j)):
            a[i][j] = "4"

import sys


sys.stdout = open("1.xls", mode="w")
for i in range(1, 150):
    print(*a[i][1:], sep="\t")


for s in range(1,66+1):
    if any(a[x][y] in "1" for x, y in f(8, s)):
        print(s)
        break
print("------------")
for s in range(1,66+1):
    if a[8][s] in "3":
        print(s)
print("------------")
for s in range(1,66+1):
    if a[8][s] in "4":
        print(s)


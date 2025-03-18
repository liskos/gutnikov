def f(x):
    return (x*3),(x+1),(x+3)

a = [[" "] * 200 for _ in range(200)]

for i in range(200):
    if i >= 61:
        a[i] = "0"

for i in range(200):
    if a[i] == " " and any(a[x] in "0" for x in f(i)):
        a[i] = "1"

for i in range(200):
    if a[i] == " " and all(a[x] in "1" for x in f(i)):
            a[i] = "2"

for i in range(200):
    if a[i] == " " and any(a[x] in "2" for x, y in f(i)):
        a[i] = "3"

for i in range(200):
    if a[i] == " " and all(a[x] in "13" for x in f(i)):
            a[i] = "4"

for s in range(1,51):
    if any(a[x] == "1" for x in f(s)):
        print(s)
        break

def f(x):
    return (x+2),(x*2)

a = [" "] * 200

for i in range(200):
    if i >= 25:
        a[i] = "0"

for i in range(200):
    if a[i] == " " and any(a[x] == "0" for x in f(i)):
        a[i] = "1"

for i in range(200):
    if a[i] == " " and all(a[x] == "1" for x in f(i)):
        a[i] = "2"

for i in range(200):
    if a[i] == " " and any(a[x] == "2" for x in f(i)):
        a[i] = "3"

for i in range(200):
    if a[i] == " " and all(a[x] in "13" for x in f(i)):
        a[i] = "4"

for s in range(1, 25):
    if any(a[x] == "1" for x in f(s)):
        print(s)
        break
print([s for s in range(1,25) if a[s] == "3"])
print([s for s in range(1,25) if a[s] == "4"])

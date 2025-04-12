def f(x):
    return (x - 3), (x - 5),(x // 4)

a = [" "] * 4000

for i in range(4000):
    if i <= 13:
        a[i] = "0"

for i in range(4000):
    if a[i] == " " and any(a[x] == "0" for x in f(i)):
        a[i] = "1"

for i in range(4000):
    if a[i] == " " and all(a[x] == "1" for x in f(i)):
        a[i] = "2"

for i in range(4000):
    if a[i] == " " and any(a[x] == "2" for x in f(i)):
        a[i] = "3"

for i in range(4000):
    if a[i] == " " and all(a[x] in "13" for x in f(i)):
        a[i] = "4"

for s in range(14, 2000):
    if any(a[x] == "1" for x in f(s)):
        print(s)
print([s for s in range(14,2000) if a[s] == "3"])
print([s for s in range(14,2000) if a[s] == "4"])
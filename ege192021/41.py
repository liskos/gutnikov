def f(x):
    return (x + 2), (x * 3)

a = [" "] * 2000

for i in range(2000):
    if i >= 50:
        a[i] = "0"

for i in range(2000):
    if a[i] == " " and any(a[x] == "0" for x in f(i)):
        a[i] = "1"

for i in range(2000):
    if a[i] == " " and all(a[x] == "1" for x in f(i)):
        a[i] = "2"

for i in range(2000):
    if a[i] == " " and any(a[x] == "2" for x in f(i)):
        a[i] = "3"

for i in range(2000):
    if a[i] == " " and all(a[x] in "13" for x in f(i)):
        a[i] = "4"

print([s for s in range(1, 50) if a[s] == "2"])
print([s for s in range(1,50) if a[s] == "3"])
print([s for s in range(1,50) if a[s] == "4"])
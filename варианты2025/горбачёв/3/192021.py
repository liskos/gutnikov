def f(x):
    return (x - 11),(x // 3)

a = [" "] * 5001

for i in range(5000):
    if i < 91:
        a[i] = "0"

for i in range(5000):
    if a[i] == " " and any(a[x] == "0" for x in f(i)):
            a[i] = "1"

for i in range(5000):
    if a[i] == " " and all(a[x] == "1" for x in f(i)):
        a[i] = "2"

for i in range(5000):
    if a[i] == " " and any(a[x] == "2" for x in f(i)):
        a[i] = "3"

for i in range(5000):
    if a[i] == " " and all(a[x] in "13" for x in f(i)):
        a[i] = "4"


print([s for s in range(91, 5001) if a[s] == "1"])
print([s for s in range(91, 5001) if a[s] == "2"])
print([s for s in range(91, 5001) if a[s] == "3"])
print([s for s in range(91, 5001) if a[s] == "4"])

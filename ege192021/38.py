def f(x):
    c = [x*3, x+1, x+3]
    b = [i for i in c if i % 2 != 0]
    return b

a = [" "] * 200

for i in range(200):
    if i >= 51:
        a[i] = "0"

for i in range(200):
    if a[i] == " " and any(a[x] in "0" for x in f(i)):
        a[i] = "1"

for i in range(200):
    if a[i] == " " and all(a[x] in "1" for x in f(i)):
            a[i] = "2"

for i in range(200):
    if a[i] == " " and any(a[x] in "2" for x in f(i)):
        a[i] = "3"

for i in range(200):
    if a[i] == " " and all(a[x] in "13" for x in f(i)):
            a[i] = "4"

for s in range(1,51):
    if any(a[x] == "1" for x in f(s)):
        print(s)
        break
print([s for s in range(1, 51) if a[s] == "3"])
print([s for s in range(1, 51) if a[s] == "4"])
print([s for s in range(1, 51) if a[s] == "1"])
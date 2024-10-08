def tr(n):
    s = ""
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s

def f(n):
    t = tr(n)
    if sum(int(x) for x in t) % 2 == 0:
        t = "1" + t + "2"
    else:
        t = "2" + t + "0"
    return int(t, 3)

print(f(4)==41)
a = []
for i in range(1, 1000):
    if f(i) > 100:
        a.append(f(i))
print(min(a))
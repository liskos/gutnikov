def f(a, b):
    return (a % 7 == 0) and (b % 17 != 0)

r = []
a = [int(x) for x in open("17data/17-1.txt")]

for i in range(len(a) - 1):
    if  f(a[i], a[i+1]) or f(a[i+1], a[i]):
        r.append(a[i] + a[i + 1])
print(len(r), min(r))
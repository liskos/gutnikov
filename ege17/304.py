a = [int(x) for x in open("17data/17-304.txt")]
r = []
m = min(a)
def f(x, y): return (x % sum(map(int, oct(y)[2:]))) == 0
for i in range(len(a) - 1):
    if (f(a[i], a[i+1]) != f(a[i+1], a[i])) and ((a[i] +a[i + 1]) % m == 0):
        r.append(a[i] + a[i + 1])
print(len(r), max(r))

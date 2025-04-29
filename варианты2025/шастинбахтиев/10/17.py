r = []
a = [int(x) for x in open("17.txt")]
min123 = min([x for x in a if x > 0 and x % 1000 == 123])
for i in range(len(a) - 1):
    if abs(a[i] - a[i + 1]) <= min123:
        r.append(abs(a[i] - a[i + 1]))
print(len(r), max(r))
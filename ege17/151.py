r = []
a = [int(x) for x in open("17data/17-1.txt")]
for i in range(len(a) - 1):
    d = [x for x in a[i: i + 2] if abs(x) % 10 == 6 and x % 3 == 0]
    if len(d) >= 1:
        r.append(min(a[i:i + 2]))
print(len(r), min(r))
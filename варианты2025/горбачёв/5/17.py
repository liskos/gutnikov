b = []
a = [int(x) for x in open("17(1).txt")]
m33 = max([x for x in a if 100 <= x < 1000 and x % 100 == 33])
for i in range(len(a)-2):
    t = a[i:i+3]
    t1 = [x for x in t if len(str(abs(x))) == 5 and str(abs(x))[-2:] == "61"]
    if len(t1) >= 1 and sum(t) >= m33:
        b.append(sum(t))
print(len(b), max(b))
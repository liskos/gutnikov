r = []
a = [int(x) for x in open("17.txt")]
k = 0
m = max(a)
for i in range(len(a) - 2):
    t = a[i:i + 3]
    otr = sum([x for x in t if x < 0])
    pol = sum([x for x in t if x > 0])

    if abs(otr) <= pol and abs(a[i] * a[i + 1] * a[i + 2]) % 10 == m % 10:
        r.append(abs(t[0] * t[1] * t[2]))
print(len(r), max(r))
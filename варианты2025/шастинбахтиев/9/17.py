r = []
a = [int(x) for x in open("17.txt")]
s4 = sum([x for x in a if len(str(abs(x))) == 4])
for i in range(len(a) - 2):
    t = a[i:i + 3]
    b = [x for x in t if len(str(abs(x))) == 3]
    if len(b) == 2 and t[0] * t[1] * t[-1] > s4:
        r.append(t[0] * t[1] * t[-1])
print(len(r), abs(min(r)))
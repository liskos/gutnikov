s = []
a = [int(x) for x in open("17.txt")]
print(a)
ch = len([x for x in a if x % 2 == 0])
for i in range(len(a) - 1):
    if (a[i] * a[i + 1] > 0) and (abs(a[i] - a[i + 1]) <= ch):
        s.append(a[i] + a[i + 1])
print(len(s), max(s))
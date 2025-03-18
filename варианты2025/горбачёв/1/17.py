a = [int(i) for i in open("17.txt")]
m = min([x for x in a if x > 0 and x % 8 == 0 and str(x)[0] == "7"])
s = []
for i in range(len(a) - 1):
    if len(str(abs(a[i]))) == 4 and len(str(abs(a[i + 1]))) == 4 and (a[i] + a[i + 1] < m):
        s.append(a[i] + a[i + 1])
print(len(s), max(s))
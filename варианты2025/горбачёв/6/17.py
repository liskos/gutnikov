a = [int(x) for x in open("17.txt")]
m7 = min([x for x in a if x % 7 == 0 and str(x)[-1] == "7"])
b = []
for i in range(len(a) - 1):
    t = a[i:i + 2]
    if (100 <= abs(a[i]) < 1000 or  100 <= abs(a[i+1]) < 1000) and a[i] + a[i+1] > m7:
        b.append(a[i]**2 + a[i+1]**2)
print(len(b), max(b))
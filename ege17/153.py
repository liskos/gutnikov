r = []
a = [int(x) for x in open("17data/17-1.txt")]
for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        r.append(abs(a[i + 1] - a[i]))
print(len(r), min(r))
sqr = [x ** 2 for x in range(1, 101)]
a = [int(x) for x in open("17data/17-294.txt")]
r = []
sr_ar = sum(a) / len(a)
for i in range(len(a) - 1):
    if ((sum(map(int, str(a[i])))) + (sum(map(int, str(a[i + 1]))))) in sqr and a[i]  + a[i + 1] > sr_ar:
        r.append(a[i] + a[i + 1])
print(len(r), max(r))

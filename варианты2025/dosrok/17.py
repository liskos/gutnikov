r = []
a = [int(x) for x in open("17.txt")]
sum_otr = sum([x for x in a if x < 0])
for i in range(len(a) - 2):
    t = a[i:i+3]
    if max(t) * min(t) > sum_otr:
        r.append(sum(t))
print(len(r), max(r))
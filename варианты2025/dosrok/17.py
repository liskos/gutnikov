r = []
a = [int(x) for x in open("17.txt")]
sum_otr = sum([x for x in a if x < 0])
for i in range(len(a) - 2):
    if max(a[i:i + 2]) * min(a[i:i + 2]) > sum_otr:
        r.append(abs(sum(a[i:i + 2])))
print(len(r), max(r))
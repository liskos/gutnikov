a = [int(x) for x in open("17data/17-7.txt")]
r = []
for i in a:
    if sum(map(int, str(i))) % 3 == 0:
        r.append(a[i])
print(len(r), max(r))

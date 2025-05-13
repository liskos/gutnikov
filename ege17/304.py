a = [int(x) for x in open("17data/17-304.txt")]
r = []
sr_ar = sum(a) / len(a)
for i in range(len(a) - 1):
    if ((a[i + 1] % sum(map(int, oct(a[i])[2:])) == 0) and (a[i] % sum(map(int, oct(a[i + 1])[2:])) != 0)) or (a[i] % sum(map(int, oct(a[i + 1])[2:])) == 0 and a[i + 1] % sum(map(int, oct(a[i])[2:])) != 0) and (sum(map(int, str(a[i]))) + sum(map(int, str(a[i + 1])))) % min(a[i:i + 2]) == 0:
        r.append(a[i] + a[i + 1])
print(len(r), max(r))

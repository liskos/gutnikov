r = []
a = [int(x) for x in open("17data/17-3.txt")]
for i in range(1, len(a) - 2):
    if sum(a[i:i + 1]) % 10 == 5 and a[i] * a[i + 1] % 7 == 0:
        r.append(sum(a[i:i+2]))
print(len(r), max(r))
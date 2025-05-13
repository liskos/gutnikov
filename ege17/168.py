s = [int(x) for x in open("17data/17-3.txt")]
r = []
for i in range(len(s) - 3):
    if (s[i] > s[i + 1] > s[i + 2] > s[i + 3]) and (s[i] - s[i + 3] > 1000):
        r.append(s[i] + s[i + 1] + s[i + 2] + s[i + 3])
print(len(r), min(r))
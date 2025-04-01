a = [int(x) for x in open("17.txt")]

r = []
for i in range(len(a) - 2):
    t = a[i:i + 3]
    t2 = [x for x in t if x % 11 == 0 and str(x)[-1] == "3"]
    if len(t2) == 2:
        r.append(2*sum(t))
print(len(r), min(r))
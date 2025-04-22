a = [int(x) for x in open("17.txt")]
para = [x for x in a if 99 < x < 1000]
for i in range(len(a) - 1):
    t = a[i:i + 2]
    t1 = [x for x in t if a[i] + a[i + 1] > min(a[i:i + 1]) and min(a[i:i + 1]) % 7 == 0 and min(a[i:i + 1]) % 10 == 7]
    if len(t1) >= 1 and sum()
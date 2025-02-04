s=[]
a = [int(x) for x in open("17.txt")]
m7 = len([x for x in a if abs(x) % 10 == 7])
for i in range(len(a) - 1):
    if a[i] * a[i + 1] < 0 and a[i] + a[i + 1] < m7:
        s.append(a[i] + a[i + 1])
print(len(s), max(s))
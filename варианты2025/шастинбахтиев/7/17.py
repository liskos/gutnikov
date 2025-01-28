answer = []
a = [int(x) for x in open("17.txt")]
m = max(a) / 2
for i in range(len(a) - 2):
    t = a[i:i+3]
    c = [x for x in t if "0" not in str(x)]
    if len(c) >= 2 and sum(t) < m:
        answer.append(sum(t))
print(len(answer), max(answer))
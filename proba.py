a = []
for i in range(11):
    x, f = input().split()
    x = int(x)
    a.append([x, f])
a.sort(key=lambda x:x[0])
print(a)

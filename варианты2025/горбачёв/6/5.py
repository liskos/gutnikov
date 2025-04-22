def sem(n):
    s = ""
    while n > 0:
        s = str(n % 7) + s
        n //= 7
    return s

def f(n):
    s = sem(n)
    if s.count("3") % 2 == 0:
        s = "3" + s + s[0]
    else:
        s = "6" + s + s[-1]
    return int(s, 7)

a = []
for i in reversed(range(1, 10000)):
    if f(i) < 16777:
        a.append(f(i))
print(max(a))
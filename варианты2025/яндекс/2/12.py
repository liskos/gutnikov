def f(n):
    while "52" in s or "2222" in s or "1112" in s:
        if "52" in s:
            s = s.replace("52", "11", 1)
            s = s.replace("2222", "5", 1)
        else:
            s.replace("1112", "2", 1)
    return s


k = 0
for n in range(4, 10000):
    s = "5" + n * "2"
    if sum([int(a) for a in s]) == 1685:
        k = n
        print(n)
print(k)
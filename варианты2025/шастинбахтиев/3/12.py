def f(s):
    while "411" in s or "1111" in s:
        if "411" in s:
            s = s.replace("411", "14", 1)
        if "1111" in s:
            s = s.replace("1111", "1", 1)
    return s



v = []
for n in range(4, 10000):
    s = "4" + "1" * n
    v.append(sum(int(x) for x in f(s)))
    if n % 100 == 0:
        print(n // 100, "%")
print(max(v))

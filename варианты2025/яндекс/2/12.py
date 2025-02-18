def f(s):
    k = 0
    while ("52" in s) or ("2222" in s) or ("1112" in s):
        if "52" in s:
            s = s.replace("52", "11", 1)
            s = s.replace("2222", "5", 1)
        else:
            s.replace("1112", "2", 1)
        k += 1
        if k > 30000:
            return "0"
    return s



for n in reversed(range(4, 4500)):
    s = "5" + n * "2"
    if sum([int(a) for a in f(s)]) == 1685:
        print(n)
        break
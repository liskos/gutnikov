
def f(s):
    while ">1" in s or ">2" in s or ">0" in s:
        s = s.replace(">1", "22>", 1)
        s = s.replace(">2", "2>", 1)
        s = s.replace(">0", "1>", 1)
    return s

for n in range(7,100):
    s = ">" + 19 * "0" + n * "1" + 19 * "2"
    x = f(s)[:-1]
    a = sum([int(a) for a in x])
    if str(a)[-1] == str(a)[-2]:
        print(n)
        break


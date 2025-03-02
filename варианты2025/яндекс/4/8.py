import itertools


s = set()
for a in itertools.product("0123456789abc", repeat=7):
    b = "".join(a)
    ss = b.replace("0", "0").replace("2", "0").replace("4", "0").replace("6", "0").replace("8", "0").replace("a", "0").replace("c", "0").replace("1", "1").replace("3", "1").replace("5", "1").replace("7", "1").replace("9", "1").replace("b", "1")
    if a.count("5") >= 2 and a[0] != "0" and "00" not in ss and "11" not in ss:
        s.add(a)
print(len(s))
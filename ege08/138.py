import itertools

s = set()
for a in itertools.product("МОИСЕЙ", repeat=4):
    b = "".join(a)
    ss = b.replace("О", "Х").replace("И", "Х").replace("Е", "Х")
    if ss.count("Х") > 0 and a[0] != "Й":
        s.add(b)
print(len(s),s )
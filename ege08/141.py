import itertools

s = set()
for a in itertools.product("БЕРКЛИЙ", repeat=4):
    b = "".join(a)
    ss = b.replace("Е", "Х").replace("И", "Х")
    if ss.count("Х") > 0 and a[0] != "Й":
        s.add(b)
print(len(s),s )
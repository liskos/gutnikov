import itertools

s = set()
for a in itertools.product("ВАЯЮЩИЙ", repeat=4):
    b = "".join(a)
    ss = b.replace("А", "Х").replace("Я", "Х").replace("Ю", "Х").replace("И", "Х")
    if ss.count("Х") > 0 and a[0] != "Й":
        s.add(b)
print(len(s),s )
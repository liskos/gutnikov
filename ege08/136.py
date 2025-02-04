import itertools

s = set()
for a in itertools.product("ГЕРОЙ", repeat=4):
    b = "".join(a)
    ss = b.replace("Е", "Х").replace("О", "Х").replace("Й", "Х")
    if ss.count("Х") > 0 and a[0] != "Й":
        s.add(b)
print(len(s),s )
import itertools

s = set()
for a in itertools.product("АЗИМУТ", repeat=6):
    b = "".join(a)
    ss = b.replace("З", "Х").replace("М", "Х").replace("Т", "Х")
    if ss.count("Х") >= 3:
        s.add(b)
print(len(s),s )
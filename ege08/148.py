import itertools

s = set()
for a in itertools.product("КАРКАС", repeat=6):
    b = "".join(a)
    ss = b.replace("К", "Х").replace("Р", "Х").replace("С", "Х")
    if ss.count("Х") >= 3:
        s.add(b)
print(len(s))
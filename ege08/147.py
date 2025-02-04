import itertools

s = set()
for a in itertools.product("КОРТИК", repeat=6):
    b = "".join(a)
    ss = b.replace("К", "Х").replace("Р", "Х").replace("Т", "Х").replace("К", "Х")
    if ss.count("Х") >= 3:
        s.add(b)
print(len(s))
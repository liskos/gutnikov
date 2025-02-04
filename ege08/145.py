import itertools

s = set()
for a in itertools.product("РАДУГА", repeat=6):
    b = "".join(a)
    ss = b.replace("Р", "Х").replace("Д", "Х").replace("Г", "Х")
    if ss.count("Х") >= 3:
        s.add(b)
print(len(s))
import itertools

s = set()
for a in itertools.product("РУСТАМ", repeat=6):
    b = "".join(a)
    ss = b.replace("Р", "Х").replace("С", "Х").replace("Т", "Х").replace("М", "Х")
    if ss.count("Х") >= 3:
        s.add(b)
print(len(s),s )
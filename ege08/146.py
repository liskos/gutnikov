import itertools

s = set()
for a in itertools.product("РАЗМАХ", repeat=6):
    b = "".join(a)
    ss = b.replace("Р", "Х").replace("З", "Х").replace("М", "Х").replace("Х", "Х")
    if ss.count("Х") >= 3:
        s.add(b)
print(len(s))
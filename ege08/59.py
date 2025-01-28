import itertools


s = set()
for a in itertools.product("ПИРОГ", repeat=5):
    b = "".join(a)
    ss = b.replace("РИ", "ХХ").replace("РО", "ХХ")
    if b.count("Р") <= 2 and "Р" not in ss:
        s.add(b)
print(len(s))
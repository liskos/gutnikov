import itertools


k = set()
for a in itertools.product("ПИРОГ", repeat=4):
    b = "".join(a)
    ss = b.replace("ПО", "XX").replace("РО", "XX").replace("ГО", "XX")
    if b.count("О") <= 2 and ("О" not in ss):
        k.add(b)
print(len(k))
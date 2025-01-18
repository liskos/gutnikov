import itertools


k = 0
for a in itertools.product("12345", repeat=4):
    b = "".join(a)
    if b.count("4") <= 2:
        if "14" in b or "34" in b or "54" in b:
            k += 1
        print(b)
print(k)
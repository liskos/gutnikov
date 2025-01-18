import itertools


k = 0
for a in itertools.product("12345", repeat=5):
    b = "".join(a)
    if "24" not in b and b.count("4") == 1 and b[0] != "4":
        k += 1
        print(b)
print(k)
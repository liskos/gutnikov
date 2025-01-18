import itertools


k = 0
for a in itertools.product("12345", repeat=6):
    b = "".join(a)
    if b.count("3") == 1 and b[-1] != "3" and ("32" in b or "34" in b):
        k += 1
        print(b)
print(k)
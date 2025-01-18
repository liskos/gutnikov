import itertools


k = 0
for a in itertools.product("МУХА", repeat=5):
    if a.count("У") <= 3 or "У" not in a:
        k += 1
        print(a)
print(k)
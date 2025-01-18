import itertools


k = 0
for a in itertools.product("КЛОУН", repeat=4):
    if "У" in a:
        k += 1
        print(a)
print(k)
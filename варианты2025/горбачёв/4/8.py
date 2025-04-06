import itertools


k = 0
for a in itertools.product("0123456", repeat=7):
    if ("035" not in a[0]) and ("246" not in a[-1]) and (a.count("0") <= 1):
        k+= 1
print(k)
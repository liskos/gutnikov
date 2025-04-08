import itertools


k = 0
for a in itertools.product("0123456", repeat=7):
    if (a[0] not in "035") and (a[-1] not in "0246") and (a.count("0") <= 1):
        k+= 1
print(k)
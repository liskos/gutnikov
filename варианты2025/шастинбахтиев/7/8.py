import itertools


s = set()
for a in itertools.product("ДИОНСЙ", repeat=6):
    if (("Д" in a) != ("Н" in a)) and (a[0] != a[1]) and (a[1] != a[2]) and (a[2] != a[3]) and (a[3] != a[4]) and (a[4] != a[5]):
        s.add(a)
print(len(s))
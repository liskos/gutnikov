import itertools


s = set()
for a in itertools.product("КРАН", repeat=3):
    if a.count("А") >= 1:
        s.add(a)
print(len(a),s)
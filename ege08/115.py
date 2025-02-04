import itertools


s = set()
for a in itertools.permutations("МАРТА", r=5):
    b = "".join(a)
    ss = b.replace("А","0")
    if "00" not in ss:
        s.add(b)
print(len(s),s)
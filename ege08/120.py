import itertools


s = set()
for a in itertools.permutations("ПРИКАЗ", r=4):
    b = "".join(a)
    ss = b.replace("А","0").replace("И", "0")
    if ss.count("0") <= 1:
        s.add(b)
print(len(s),s)
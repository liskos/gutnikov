import itertools


d = set()
for a in itertools.permutations("01234567", r=7):
    s = "".join(a)
    ss = s.replace("3","1").replace("5", "1").replace("7", "1")
    ss = ss.replace("2", "0").replace("4", "0").replace("6", "0")
    if "00" not in ss and "11" not in ss and a[0] != "0":
        d.add(a)
print(len(d))
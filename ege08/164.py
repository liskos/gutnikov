import itertools


d = set()
for a in itertools.permutations("0123456789101112131415", r=3):
    s = "".join(a)
    ss = s.replace("3","1").replace("5", "1").replace("7", "1").replace("9", "1").replace("11", "1").replace("13", "1").replace("15", "1")
    ss = ss.replace("2", "0").replace("4", "0").replace("6", "0").replace("8", "0").replace("10", "0").replace("12", "0").replace("14", "0")
    if "00" not in ss and "11" not in ss and a[0] != "0":
        d.add(a)
print(len(d))
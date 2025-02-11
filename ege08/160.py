import itertools


s = set()
for a in itertools.permutations("01234567",r=5):
    b = "".join(a)
    ss = b.replace("2", "0").replace("4", "0").replace("6", "0").replace("3", "1").replace("5", "1").replace("7", "1")
    if a[0] != "0" and (ss == "10101" or ss == "01010"):
        s.add(b)
print(len(s))
import itertools


s = set()
for a in itertools.permutations("01234567",r=6):
    b = "".join(a)
    ss = b.replace("2", "0").replace("4", "0").replace("6", "0").replace("3", "1").replace("5", "1").replace("7", "1")
    if a[0] != "0" and (ss == "101010" or ss == "010101"):
        s.add(b)
print(len(s))
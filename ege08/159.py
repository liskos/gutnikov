import itertools


s = set()
for a in itertools.permutations("0123456789",r=8):
    b = "".join(a)
    ss = b.replace("2", "0").replace("4", "0").replace("6", "0").replace("8", "0").replace("3", "1").replace("5", "1").replace("7", "1").replace("9", "1")
    if a[0] != "0" and int(b) % 5 == 0 and (ss == "10101010" or ss == "01010101"):
        s.add(b)
print(len(s))
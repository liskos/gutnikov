import itertools


s = set()
for a in itertools.permutations("ПАРИЖАНКА", r=9):
    b = "".join(a)
    ss = b.replace("А", "Х").replace("И", "Х")
    if "ХХХ" not in ss and ss.count("ХХ") == 1:
        s.add(b)
print(len(s),s )
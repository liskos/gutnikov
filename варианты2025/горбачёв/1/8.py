import itertools


s = set()
for a in itertools.permutations("01234567", r=6):
    b = "".join(a)
    if "54" not in b and "26" in b and "0" != b[0]:
        s.add(b)
print(len(s))

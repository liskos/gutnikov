import itertools

s = set()
for a in itertools.permutations("ВОРОН", r=5):
    b = "".join(a)
    ss = b.replace("О", "Х")
    if "ХХ" not in ss:
        s.add(b)
print(len(s),s)
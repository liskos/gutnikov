import itertools

s = set()
for a in itertools.permutations("АРЕАЛ", r=5):
    b = "".join(a)
    ss = b.replace("А", "Х").replace("Е", "Х")
    if "ХХ" not in ss:
        s.add(b)
print(len(s),s )
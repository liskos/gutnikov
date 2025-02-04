import itertools

s = set()
for a in itertools.permutations("АПОРТ", r=5):
    b = "".join(a)
    ss = b.replace("А", "Х").replace("О", "Х")
    if "ХХ" not in ss:
        s.add(b)
print(len(s),s )
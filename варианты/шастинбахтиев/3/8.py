import itertools
s = set()
for i, a in enumerate(itertools.product("ЕЛОПРСТ", repeat=5),1):
    if i % 2 == 1 and a[-1] in "ЕО" and (a.count("Л") + a.count("П") + a.count("Р") + a.count("С") + a.count("Т")) < 4:
        s.add(a)
print(len(s), s)
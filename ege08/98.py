import itertools


s = set()
for a in itertools.permutations("ГЕЛИЙ", r=5):
    if a[0] != "Й" and "ИЕЙ" not in "".join(a):
        s.add(a)
print(len(s))
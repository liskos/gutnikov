import itertools


s = set()
for a in itertools.permutations("НОБЕЛИЙ", r=7):
    if a[0] != "Й" and "ИЙО" not in "".join(a):
        s.add(a)
print(len(s))
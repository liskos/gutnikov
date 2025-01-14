import itertools


d = set()
for a in itertools.product("МАРИН", repeat=8):
    s = "".join(a)
    if set(s[:4]) == {"М", "А", "Р", "И"} and set(s[-4:]) <= {"И", "Н", "А"}:
        d.add(s)
d = sorted(d)
for i, a in enumerate(d, 1):
    if a == "МАРИАННА":
        print(i,a)
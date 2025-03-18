s = "a" * 131
while "aaaa" in s or "bbb" in s:
    if "aaaa" in s:
        s = s.replace("aaaa", "b", 1)
    else:
        s = s.replace("bbb", "aa", 1)
print(s)
z = set()
for k in range(1, 100):
    for j in range(1, 100):
        s = "7" + "8" * k + "9" * j
        while "78" in s or "98" in s or "999" in s:
            if "78" in s: s = s.replace("78", "8", 1)
            if "98" in s: s = s.replace("98", "7", 1)
            if "999" in s: s = s.replace("999", "9", 1)
        if sum(map(int, s)) == 801:
            print(len(s))
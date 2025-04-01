for n in reversed(range(1, 1000)):
    s = "-" + "+" * n
    while "-+" in s or "2++" in s or "++++" in s:
        if "-+" in s: s = s.replace("-+", "2+", 1)
        if "2++" in s: s = s.replace("2++", "--", 1)
        if "++++" in s: s = s.replace("++++", "22", 1)
    if s.count("+") + s.count("-") == 251:
            print(n)
            break
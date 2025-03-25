for n in reversed(range(1, 2500)):
    s = "=" + 51 * "3" + n * "4" + 53 * "5"
    while "=3" in s or "=4" in s or "=5" in s:
        if "=3" in s: s = s.replace("=3", "55=", 1)
        if "=4" in s: s = s.replace("=4", "4=", 1)
        if "=5" in s: s = s.replace("=5", "3=", 1)
    if 1000 <= sum(map(int, s[:-1])) <= 9999:
        print(n)
        break
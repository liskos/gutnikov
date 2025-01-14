s = 90 * "1"
while "1111" in s or "000" in s:
    if "1111" in s:
        s = s.replace("1111", "10000", 1)
    else:
        s = s.replace("000", "11", 1)
print(s.count("1"),s.count("0"))
s = "1" + 51 * "2"
while "12" in s or "1" in s:
    if "12" in s:
        s = s.replace("12", "2221", 1)
    else:
        s = s.replace("1", "222222", 1)
print(s.count("2"))
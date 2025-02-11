s = ">" + 19*"0" n*"1" + 19*"2"
while ">1" in s or ">2" in s or ">0" in s:
    s = s.replace(">1", "22>", 1)
    s = s.replace(">2", "2>", 1)
    s = s.replace(">0", "1>", 1)
print(s)
x = (7 ** 160 * 7 ** 90) - (14 ** 150 + 2 ** 13)
s = ""
while x > 0:
    s = str(x%7) + s
    x //= 7
s = s.replace("6", "0")
print(sum(map(int, s)))
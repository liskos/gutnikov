m = 5 * 729 ** 2024 + 3 * 243 ** 1413 - 7 * 81 ** 169 + 3017 - 2 * 9 ** 107
s = []
while m > 0:
    s.append(m % 27)
    m //= 27
a = [x for x in s if x <= 25 and x % 2 == 0]
print(sum(a))
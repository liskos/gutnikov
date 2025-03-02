# 221n + 348 = 180n + 2
# 221n = 2* n ** 2 + 2 * n + 1
# 348 = 3 * 8 + 4
# 180 n + 2 = n** 2 + 4 * n + 4 + 8 * n + 16
for n in range(1,40):
    if 2 * n ** 2 + 2 * n + 1 + 3 * 8 + 4 == n ** 2 + 4 * n + 4 + 8 * n + 16:
        print(n)

for n in range(1, 40):
    try:
        if int("221", n) + int("34", 8) == int("180", n + 2):
            print(n)
    except:
        pass
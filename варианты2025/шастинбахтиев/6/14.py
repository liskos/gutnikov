for x in range(0,25):
    s = int("A407F2", 25) + x * 25 ** 3 + int("N0G50H", 25) + x * 25 ** 1 + x * 25 ** 4 + int("740M26", 25) + x * 25 ** 3
    if s % 24 == 0:
        print(s // 24)
for x in range(21):
    f = f"82934{x}2"
    s = f"2924{x}{x}7"
    t = f"67564{x}8"
    z = int(f, 21) + int(s, 21) + int(t, 21)
    if z % 20 == 0:
        print(z // 20)

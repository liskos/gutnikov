for a in range(0, 1000):
    if all([(((3 * x + y) > a) and (y < x) and (x < 30)) == False for x in range(0, 200) for y in range(0, 200)]):
        print(a)
        break

def f(x):
    while ("01" in x) or ("02" in x) or ("03" in x):
        x = x.replace("01", "30", 1)
        x = x.replace("02", "3103", 1)
        x = x.replace("03", "1201", 1)
    return x

for x in range(1, 47):
    for y in range(1, 47):
        for z in range(1, 47):
            s = "0" + x * '1' + y * "2" + z * "3"
            v = f(s)
            if (v.count("1") == 31) and (v.count("2") == 24) and (v.count("3") == 46):
                print(x, y, z)
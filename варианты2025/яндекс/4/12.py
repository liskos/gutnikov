for x in range(1,50):
    for y in range(1, 50):
        for z in range(1, 50):
            s = ">" + x * "1" + y * "2" + z * "3"
            while ">1" in s or ">2" in s or ">3" in s:
                s = s.replace(">1","21>3", 1)
                s = s.replace(">2", "32>", 1)
                s = s.replace(">3", "11>2", 1)
            if s.count("1") == 71 and s.count("2") == 54 and s.count("3") == 37:
                print(x,y,z)
for n in range(1, 40):
    try:
        if int("132", n) + int(oct(13)[2:]) == int("124", n + 1):
            print(n)
    except:
        pass
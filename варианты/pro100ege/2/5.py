def f(x):
    s = []
    while x > 0:
        s.append(str(x % 3))
        x //= 3
    if x % 2 == 0:
        s = "1" + s + '00'
    else:

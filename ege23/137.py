def f(a, b):
    if a == b:
        return 1
    if len(a) < len(b):
        return 0
    if a.count("1") == 1:
        return f(bin(int(a, 2) - 1)[2:], b)
    return f(bin(int(a, 2) - 1)[2:], b) + f("1" + (len(a) - 1) * "0", b)
print(f("1100", "100"))
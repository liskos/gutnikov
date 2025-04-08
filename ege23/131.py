def f(a:str, b:str):
    if a == b:
        return 1
    if len(a) > len(b):
        return 0
    return f(a + "0", b) + f(a + "1", b) + f(bin(int(a, 2) + 1)[2:], b)
print(f("100", "11101"))
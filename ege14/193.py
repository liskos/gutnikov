x = 4 ** 511 + 2 ** 511 - 511
a = bin(x)[2:]
print(a.count("1"))
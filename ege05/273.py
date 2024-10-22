def f(n):
    b = bin(n)[2:]
    if n % 2 == 1:
        b = "1" + b + "0"
    else:
        b = "11" + b + "11"
    return int(b, 2)


for i in range(1, 10000000000000):
    if f(i) < 10000000000:
        print(f(i))
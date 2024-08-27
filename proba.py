def func(s):
    d = int(input())
    n = 24
    s = 12
    while s <= 3004:
        s = s + d
        n = n + 3
    return n


x = 0
while True:
    x += 1
    if func(x) == 75:
        print(x)
        break


x, y = map(int, input().split())
resta(x, y)

import math
for x in range(1,100):
    for n in range(1,40):
        try:
            if x ** 2 - int("30", n) * x + int("240", n) == 0:
                print(math.sqrt(x))
                print(n)
        except:
            pass
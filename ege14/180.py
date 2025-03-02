#214n = 165n + 1
#2n**2 + n + 4 = n + 1 + 6n + 6 + 5

for i in range(1,40):
    if 2 * i ** 2 + i + 4 == i ** 2 + 2 * i + 1 + 6 * i + 6 + 5:
        print(i)

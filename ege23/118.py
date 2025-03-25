a = {1}
for i in range(6):
    b = set()
    for x in a:
        b.add(x+1)
        b.add(x+2)
        b.add(x*2)
    a = b.copy()
print(len([i for i in a if 34 <= i <= 59]))
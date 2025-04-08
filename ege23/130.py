a = {10}
for _ in range(5):
    b = set()
    for x in a:
        b.add(x + 2)
        b.add(x + 3)
        b.add(x * 2)
    a = b.copy()
print(len(a))
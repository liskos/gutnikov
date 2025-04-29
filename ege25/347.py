# def f(n):
#     a = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             a.add(i)
#             a.add(n // i)
#             if len(a) >= 4:
#                 break
#     if len(a) < 2:
#         return 0
#     a = sorted(a, reverse=True)
#     return a[0] + a[1]
#
# r = []
# for n in range(256123000, 256234001):
#     m = f(n)
#     if m % 10000 == 1234:
#         r.append([n, m])

r = [[256148312, 192111234], [256153623, 108671234], [256164673, 41234], [256182933, 85531234], [256186145, 60071234], [256202495, 66311234], [256228312, 192171234], [256232121, 96551234]]
r.sort(key=lambda x:x[1] ,reverse=True)
for x in r:
    print(*x)
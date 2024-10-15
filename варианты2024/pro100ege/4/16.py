v = [0] * 39
v[1] = 1
v[2] = 2
for i in range(3, 39):
    if i % 2 == 1:
        v[i] = v[i - 1] + v[i - 2] + 1
    else:
        v[i] = sum(v[1:i])
print(v[38])
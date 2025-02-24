import ipaddress


k = 0
net = ipaddress.ip_network(f'140.19.96.0/255.255.248.0', 0)
for ip in net:
    b = f'{ip:b}'
    p = b[:8]
    v = b[8:16]
    t = b[16:24]
    c = b[-8:]
    if p.count("1") == v.count("1") == t.count("1") == c.count("1"):
        k += 1
print(k)
import ipaddress


k = 0
net = ipaddress.ip_network(f'216.130.64.0/255.255.192.0', 0)
for ip in net:
    b = f'{ip:b}'
    p = b[:8]
    v = b[8:16]
    t = b[16:24]
    c = b[-8:]
    if p[-1] != "1" and v[-1] != "1" and t[-1] != "1" and c[-1] != "1":
        k += 1
print(k)
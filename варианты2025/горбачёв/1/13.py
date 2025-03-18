import ipaddress


k = 0
net = ipaddress.ip_network(f"232.116.0.0/255.255.240.0", 0)
for ip in net:
    a = f'{ip:b}'
    if a.count("1") % 4 == 0:
        k += 1
print(k)
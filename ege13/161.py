import ipaddress


k = 0
net = ipaddress.ip_network(f'202.75.38.176/255.255.255.240', 0)
for ip in net:
    b = f'{ip:b}'
    if "111" not in b and "000" not in b:
        k += 1
print(k)
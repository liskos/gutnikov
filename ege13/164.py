import ipaddress


k = 0
net = ipaddress.ip_network(f'202.75.38.152/255.255.255.248', 0)
for ip in net:
    b = f'{ip:b}'
    if "111" in b:
        k += 1
print(k)
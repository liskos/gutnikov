import ipaddress


k = 0
net = ipaddress.ip_network(f'184.178.54.144/255.255.255.240', 0)
for ip in net:
    b = f'{ip:b}'
    if "111" in b:
        k += 1
print(k)
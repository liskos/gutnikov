import ipaddress


k = 0
net = ipaddress.ip_network(f'0.0.0.0/255.255.128.0', 0)
for ip in net:
    b = f'{ip:b}'
    if int(b) % 4 == 0:
        k += 1
print(k)
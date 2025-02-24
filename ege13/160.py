import ipaddress


k = 0
net = ipaddress.ip_network(f'211.48.136.64/255.255.255.224', 0)
for ip in net:
    b = f'{ip:b}'
    if b[-1] == "1" and b[-2] == "1":
        k += 1
print(k)
import ipaddress


k = 0
net = ipaddress.ip_network(f'158.132.161.128/255.255.255.128', 0)
for ip in net:
    b = f'{ip:b}'
    if b[-1] == "1":
        k += 1
print(k)
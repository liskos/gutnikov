import ipaddress


k = 0
net = ipaddress.ip_network(f'192.168.248.176/255.255.255.240', 0)
for ip in net:
    b = f'{ip:b}'
    if b.count("1") > b.count("0"):
        k += 1
print(k)
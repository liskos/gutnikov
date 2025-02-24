import ipaddress


k = 0
net = ipaddress.ip_network("172.30.0.0/255.254.0.0", 0)
for ip in net:
    b = f'{ip:b}'
    if b.count("1") % 12 != 0:
        k += 1
print(k)
import ipaddress


k = 0
net = ipaddress.ip_network("192.168.248.176/255.255.255.240", 0)
for ip in net:
    ip1 = f'{ip:b}'
    if ip1.count("1") == ip1.count("0"):
        k += 1
print(k)
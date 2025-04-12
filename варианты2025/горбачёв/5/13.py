import ipaddress

k = 0
net = ipaddress.ip_network("222.119.45.0/255.255.224.0", 0)
for ip in net:
    b = f"{ip:b}"
    if b.count("0") % 3 == 0:
        k += 1
print(k)
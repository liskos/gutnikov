import ipaddress


k = 0
net = ipaddress.ip_network("82.230.106.168/255.255.255.240", 0)
for ip in net:
    b = f"{ip:b}"
    if b[8:-8].count("1") % 3 == 0:
        k += 1
print(k)
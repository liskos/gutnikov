import ipaddress


k = 0
net = ipaddress.ip_network("140.116.194.0/255.255.240.0", 0)
for ip in net:
    b = f"{ip:b}"
    if b[7] == b[15] == b[23] == b[31] == "0":
        k += 1
print(k)
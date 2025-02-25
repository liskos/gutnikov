import ipaddress


k = 0
net = ipaddress.ip_network(f'139.75.100.0/255.255.252.0', 0)
for ip in net:
    b = ip.packed[3]
    for i in range(1, 30):
        if b == 2 ** i - 1:
            k += 1
print(k)
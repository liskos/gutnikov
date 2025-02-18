import ipaddress


for mask in range(10,31):
    net = ipaddress.ip_network(f"111.91.200.28/{mask}", 0)
    print(net, 32 - mask)
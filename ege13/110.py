import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"18.168.250.32/{mask}", 0)
    print(net)
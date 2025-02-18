import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"133.57.64.130/{mask}", 0)
    print(net)
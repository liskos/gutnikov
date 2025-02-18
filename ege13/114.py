import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"132.47.160.46/{mask}", 0)
    print(net)
import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"124.145.64.28/{mask}", 0)
    print(net)
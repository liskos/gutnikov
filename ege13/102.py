import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"120.120.120.35/{mask}", 0)
    print(net)
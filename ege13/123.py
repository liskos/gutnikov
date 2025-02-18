import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"116.123.64.53/{mask}", 0)
    print(net)
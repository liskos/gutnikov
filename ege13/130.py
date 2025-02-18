import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"156.133.216.35/{mask}", 0)
    print(net, 2 ** (32 - mask))
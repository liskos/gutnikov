import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"156.32.140.138/{mask}", 0)
    print(net)
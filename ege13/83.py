import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"115.12.69.38/{mask}", 0)
    print(net)
import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"199.92.65.189/{mask}", 0)
    print(net)
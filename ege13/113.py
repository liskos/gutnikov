import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"169.97.112.115/{mask}", 0)
    print(net)
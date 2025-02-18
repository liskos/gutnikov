import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"20.24.110.42/{mask}", 0)
    print(net)
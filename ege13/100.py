import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"215.118.70.47/{mask}", 0)
    print(net)
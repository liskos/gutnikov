import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"193.138.70.47/{mask}", 0)
    print(net)
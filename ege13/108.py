import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"218.217.212.15/{mask}", 0)
    print(net)
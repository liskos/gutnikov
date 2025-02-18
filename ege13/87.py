import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"148.195.140.28/{mask}", 0)
    print(net)
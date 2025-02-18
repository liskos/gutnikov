import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"131.149.64.13/{mask}", 0)
    print(net)
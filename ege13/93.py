import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"192.75.64.98/{mask}", 0)
    print(net)
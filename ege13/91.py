import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"108.87.113.106/{mask}", 0)
    print(net)
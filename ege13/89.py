import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"118.105.136.60/{mask}", 0)
    print(net)
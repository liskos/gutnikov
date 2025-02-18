import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"194.162.77.94/{mask}", 0)
    print(net)
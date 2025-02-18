import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"208.207.230.65/{mask}", 0)
    print(net)
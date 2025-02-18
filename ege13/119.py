import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"159.152.66.19/{mask}", 0)
    print(net)
import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"214.224.120.40/{mask}", 0)
    print(net)
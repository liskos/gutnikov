import ipaddress


for mask in range(10,31):
    net = ipaddress.ip_network(f"175.122.80.13/{mask}", 0)
    print(net, net.netmask)
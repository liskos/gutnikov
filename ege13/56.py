import ipaddress


for mask in range(33):
    net = ipaddress.ip_network(f"153.209.31.240/{mask}", 0)
    print(net, net.netmask)

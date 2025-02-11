import ipaddress


for mask in range(33):
    net = ipaddress.ip_network(f"248.228.60.240/{mask}", 0)
    print(net, net.netmask)
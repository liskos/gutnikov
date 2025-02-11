import ipaddress


for mask in range(33):
    net = ipaddress.ip_network(f"148.228.120.242/{mask}", 0)
    print(net, net.netmask)
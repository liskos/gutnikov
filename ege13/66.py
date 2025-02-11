import ipaddress


for mask in range(33):
    net = ipaddress.ip_network(f"214.228.114.203/{mask}", 0)
    print(net, net.netmask)

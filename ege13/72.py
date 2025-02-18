import ipaddress


for mask in range(1, 31):
    net = ipaddress.ip_network(f"112.117.107.70/{mask}", 0)
    print(net, net.netmask)
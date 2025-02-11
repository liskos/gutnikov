import ipaddress


for mask in range(33):
    net = ipaddress.ip_network(f"117.191.88.37/{mask}", 0)
    print(net, net.netmask)

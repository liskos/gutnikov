import ipaddress


for mask in range(33):
    net = ipaddress.ip_network(f"145.192.94.230/{mask}", 0)
    print(net, net.netmask)

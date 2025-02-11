import ipaddress


for mask in range(33):
    net = ipaddress.ip_network(f"135.116.177.140/{mask}", 0)
    print(net, net.netmask)

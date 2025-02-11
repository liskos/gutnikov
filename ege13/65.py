import ipaddress


for mask in range(33):
    net = ipaddress.ip_network(f"220.128.114.142/{mask}", 0)
    print(net, net.netmask)

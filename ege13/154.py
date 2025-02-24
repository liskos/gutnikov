import ipaddress


for mask in range(10,31):
    net = ipaddress.ip_network(f"125.28.160.73/{mask}", 0)
    print(net, net.netmask)
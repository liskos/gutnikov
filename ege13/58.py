import ipaddress


for mask in range(33):
    net = ipaddress.ip_network(f"134.92.108.145/{mask}", 0)
    print(net, net.netmask)

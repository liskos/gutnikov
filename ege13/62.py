import ipaddress


for mask in range(33):
    net = ipaddress.ip_network(f"158.198.228.220/{mask}", 0)
    print(net, net.netmask)

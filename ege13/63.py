import ipaddress


for mask in range(33):
    net = ipaddress.ip_network(f"124.32.48.131/{mask}", 0)
    print(net, net.netmask)

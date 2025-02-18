import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"111.81.208.27/{mask}", 0)
    print(net, net.netmask)
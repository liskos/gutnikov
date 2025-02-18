import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"215.181.200.27/{mask}", 0)
    print(net, net.netmask)
import ipaddress


for mask in range(10,31):
    net = ipaddress.ip_network(f"188.214.176.25/{mask}", 0)
    print(net, net.netmask)
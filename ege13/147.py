import ipaddress


for mask in range(10,31):
    net1 = ipaddress.ip_network(f"191.131.175.201/{mask}", 0)
    net2 = ipaddress.ip_network(f"191.131.160.170/{mask}", 0)
    if net1 != net2:
        print(net1, net1.netmask)
import ipaddress


for mask in range(10,31):
    net1 = ipaddress.ip_network(f"193.175.175.231/{mask}", 0)
    net2 = ipaddress.ip_network(f"193.175.176.118/{mask}", 0)
    if net1 != net2:
        print(net1, net1.netmask)
import ipaddress


for mask in range(10,31):
    net1 = ipaddress.ip_network(f"117.137.104.11/{mask}", 0)
    net2 = ipaddress.ip_network(f"117.137.107.95/{mask}", 0)
    if net1 != net2:
        print(net1, net1.netmask)
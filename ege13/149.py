import ipaddress


for mask in range(10,31):
    net1 = ipaddress.ip_network(f"112.74.161.2/{mask}", 0)
    net2 = ipaddress.ip_network(f"112.74.98.15/{mask}", 0)
    if net1 != net2:
        print(net1, net1.netmask)
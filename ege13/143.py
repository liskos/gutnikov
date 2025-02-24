import ipaddress


for mask in range(10,33):
    net1 = ipaddress.ip_network(f"156.77.32.127/{mask}", 0)
    net2 = ipaddress.ip_network(f"156.77.117.78/{mask}", 0)
    if net1 != net2:
        print(net1, net1[-1])
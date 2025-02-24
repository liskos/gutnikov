import ipaddress


for mask in range(10,31):
    net1 = ipaddress.ip_network(f"132.46.175.26/{mask}", 0)
    net2 = ipaddress.ip_network(f"132.46.170.130/{mask}", 0)
    ip1 = ipaddress.ip_address("132.46.175.26")
    ip2 = ipaddress.ip_address("132.46.170.130")
    if ip1 not in net2 and ip2 not in net1:
        print(net1, net2, net1[-1], net2[-1])
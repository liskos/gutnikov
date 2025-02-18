import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"151.172.115.121/{mask}", 0)
    net2 = ipaddress.ip_network(f"151.172.115.156/{mask}", 0)
    ip1 = ipaddress.ip_address("151.172.115.121")
    ip2 = ipaddress.ip_address("151.172.115.156")
    if ip1 not in net2 and ip2 not in net:
        print(net, net2, net[-1], net2[-1])
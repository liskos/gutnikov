import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"115.127.30.120/{mask}", 0)
    print(net, net.netmask)
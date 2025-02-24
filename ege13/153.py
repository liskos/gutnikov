import ipaddress


for mask in range(10,31):
    net = ipaddress.ip_network(f"115.53.128.88/{mask}", 0)
    print(net, net.netmask)
import ipaddress


for mask in range(10,31):
    net = ipaddress.ip_network(f"111.3.161.27/{mask}", 0)
    print(net, net.netmask)
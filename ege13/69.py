import ipaddress


for mask in range(33):
    net = ipaddress.ip_network(f"217.138.127.144/{mask}", 0)
    print(net, net.netmask)

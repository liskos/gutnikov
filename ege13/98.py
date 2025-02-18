import ipaddress


for mask in range(10,31):
    net = ipaddress.ip_network(f"154.28.80.25/{mask}", 0)
    ip = ipaddress.ip_address("154.28.90.25")
    if ip in net:
        print(net, net[0], net[-1], 32 - mask)
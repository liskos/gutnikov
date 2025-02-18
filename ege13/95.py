import ipaddress


for mask in range(10,31):
    net = ipaddress.ip_network(f"241.185.253.57/{mask}", 0)
    print(net, 32 - mask)
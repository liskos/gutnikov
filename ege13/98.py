import ipaddress


for mask in range(10,31):
    net = ipaddress.ip_network(f"154.28.80.25/{mask}", 0)
    print(net, 32 - mask)
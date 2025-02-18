import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"221.117.97.115/{mask}", 0)
    print(net, 32 - mask)
import ipaddress


for mask in range(10,31):
    net = ipaddress.ip_network(f"204.108.112.142/{mask}", 0)
    print(net, 32 - mask)
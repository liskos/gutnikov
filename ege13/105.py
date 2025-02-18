import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"125.181.67.15/{mask}", 0)
    print(net, 32 - mask)
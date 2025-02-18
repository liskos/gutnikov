import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"212.168.104.5/{mask}", 0)
    print(net, 32 - mask)
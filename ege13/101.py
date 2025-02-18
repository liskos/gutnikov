import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"220.127.169.27/{mask}", 0)
    print(net)
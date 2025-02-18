import ipaddress


for mask in range(10, 31):
    net = ipaddress.ip_network(f"163.232.136.60/{mask}", 0)
    print(net)
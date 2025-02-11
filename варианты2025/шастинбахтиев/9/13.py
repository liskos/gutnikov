import ipaddress


for mask in range(33):
    net = ipaddress.ip_network(f"111.233.75.16/{mask}", 0)
    if net == "111.233.75.0":
        print()
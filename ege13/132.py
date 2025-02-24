import ipaddress


for mask in range(10, 31):
    net1 = ipaddress.ip_network(f"112.117.107.70/{mask}", 0)
    net2 = ipaddress.ip_network(f"112.117.121.80/{mask}", 0)
    ip1 =
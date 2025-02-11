import ipaddress


net = ipaddress.ip_network(f"126.185.90.162/255.255.252.0", 0)
print(net)
ip1 = ipaddress.ip_address("126.185.90.162")
ip2 = ipaddress.ip_address("126.185.88.0")
print(int(ip1) - int(ip2))
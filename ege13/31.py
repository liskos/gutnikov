import ipaddress


net = ipaddress.ip_network(f"192.168.156.235/255.255.255.240", 0)
print(net)
ip1 = ipaddress.ip_address("192.168.156.235")
ip2 = ipaddress.ip_address("192.168.156.224")
print(int(ip1) - int(ip2))
import ipaddress


net = ipaddress.ip_network(f"156.132.15.138/255.255.252.0", 0)
print(net)
ip1 = ipaddress.ip_address("156.132.15.138")
ip2 = ipaddress.ip_address("156.132.12.0")
print(int(ip1) - int(ip2))
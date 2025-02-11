import ipaddress


net = ipaddress.ip_network(f"156.128.0.227/255.255.255.248", 0)
print(net)
ip1 = ipaddress.ip_address("156.128.0.227")
ip2 = ipaddress.ip_address("156.128.0.224")
print(int(ip1) - int(ip2))
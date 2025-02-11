import ipaddress


net = ipaddress.ip_network(f"132.126.150.18/255.255.240.0", 0)
print(net)
ip1 = ipaddress.ip_address("132.126.150.18")
ip2 = ipaddress.ip_address("132.126.144.0")
print(int(ip1) - int(ip2))
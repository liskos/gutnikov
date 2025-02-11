import ipaddress


net = ipaddress.ip_network(f"122.191.12.189/255.255.255.128", 0)
print(net)
ip1 = ipaddress.ip_address("122.191.12.189")
ip2 = ipaddress.ip_address("122.191.12.128")
print(int(ip1) - int(ip2))
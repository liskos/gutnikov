import ipaddress


net = ipaddress.ip_network(f"206.158.124.67/255.255.224.0", 0)
print(net)
ip1 = ipaddress.ip_address("206.158.124.67")
ip2 = ipaddress.ip_address("206.158.96.0")
print(int(ip1) - int(ip2))
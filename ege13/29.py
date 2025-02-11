import ipaddress


net = ipaddress.ip_network(f"162.198.0.157/255.255.255.224", 0)
print(net)
# 162.198.0.128/27
ip1 = ipaddress.ip_address("162.198.0.157")
ip2 = ipaddress.ip_address("162.198.0.128")
print(int(ip1) - int(ip2))
import ipaddress


net = ipaddress.ip_network(f"112.154.133.208/255.255.248.0", 0)
print(net)
ip1 = ipaddress.ip_address("112.154.133.208")
ip2 = ipaddress.ip_address("112.154.128.0")
print(int(ip1) - int(ip2))
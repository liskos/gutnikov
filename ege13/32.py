import ipaddress


net = ipaddress.ip_network(f"10.18.134.220/255.255.255.192", 0)
print(net)
ip1 = ipaddress.ip_address("10.18.134.220")
ip2 = ipaddress.ip_address("10.18.134.192")
print(int(ip1) - int(ip2))
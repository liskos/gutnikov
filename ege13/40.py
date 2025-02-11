import ipaddress


net = ipaddress.ip_network(f"0.0.0.0/255.255.255.128", 0)
print(net.num_addresses - 2)
import ipaddress


net = ipaddress.ip_network(f"158.214.121.40/255.255.255.224", 0)
print(*net)
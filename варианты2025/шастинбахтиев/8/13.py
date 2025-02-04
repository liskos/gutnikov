import ipaddress


for m in range(10,32):
    net1 = ipaddress.ip_network(f"158.214.121.40/{m}", 0)
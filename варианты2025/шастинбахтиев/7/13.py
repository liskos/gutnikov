import ipaddress


for m in range(10,32):
    net1 = ipaddress.ip_network(f"200.154.190.12/{m}", 0)
    ip = ipaddress.ip_address("200.154.184.0")
    if ip in net1:

        print(net1)
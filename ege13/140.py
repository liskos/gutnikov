import ipaddress


for mask in range(10,33):
    net1 = ipaddress.ip_network(f"112.166.78.114/{mask}", 0)
    net2 = ipaddress.ip_network(f"112.166.78.117/{mask}", 0)
    ip1 = ipaddress.ip_address("112.166.78.114")
    ip2 = ipaddress.ip_address("112.166.78.117")
    if ip1 not in net2 and ip2 not in net1:
        print(net1,net2,net1[-1],net2[-1])
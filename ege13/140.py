import ipaddress


for mask in range(10,33):
    net1 = ipaddress.ip_network(f"112.166.78.114/{mask}", 0)
    net2 = ipaddress.ip_network(f"112.166.78.117/{mask}", 0)
    if net1 != net2:
        print(net1,net2,net1[-1],net2[-1])
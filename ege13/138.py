import ipaddress


for mask in range(10,31):
    net1 = ipaddress.ip_network(f"157.127.182.76/{mask}", 0)
    net2 = ipaddress.ip_network(f"157.127.190.80/{mask}", 0)
    ip1 = ipaddress.ip_address("157.127.182.76")
    ip2 = ipaddress.ip_address("157.127.190.80")
    if ip1 not in net2 and ip2 not in net1:
        print(net1, net2, net1[-1], net2[-1])
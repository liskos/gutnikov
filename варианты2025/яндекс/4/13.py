import ipaddress


for mask in range(10,31):
    net1 = ipaddress.ip_network(f"61.58.73.42/{mask}", 0)
    net2 = ipaddress.ip_network(f"61.58.75.136/{mask}", 0)
    ip1 = ipaddress.ip_address("61.58.73.42")
    ip2 = ipaddress.ip_address("61.58.75.136")
    if ip1 in net2 and ip2 in net1:
        k = 0
        for ip in net1:
            b = f"{ip:b}"
            if b.count("1") % 2 != 0:
                k+=1
        print(mask, k)

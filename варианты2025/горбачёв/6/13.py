import ipaddress


for a in range(0, 256):
    net = ipaddress.ip_network(f"135.{a}.170.5/255.255.0.0", 0)
    for ip in net:
        if ip.packed[0].__format__("b").count("1") +  ip.packed[1].__format__("b").count("1") <= 10:
            break
    else:
        print(a)
        break
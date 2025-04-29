import ipaddress


for mask in range(31):
    net = ipaddress.ip_network(f"221.142.14.0/{mask}", 0)
    if net.num_addresses >= 8000:
        print(net, mask)
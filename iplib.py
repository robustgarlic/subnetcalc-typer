
import ipaddress
from helpers import MyIPv4
import time



def IPv4subnetted(ifc, more):    
    ip = ipaddress.IPv4Address(ifc.ip)
    network = ipaddress.IPv4Network(ifc.network)
    hosts_list = list(network.hosts())
    res =  [ hosts_list[i] for i in (0, -1) ]
    print(f'\n\nCalcuatating the Subnet......')
    time.sleep(2)

    print(f'IP Address: {ip}', 'Subnet Mask: ',network.netmask)
    print("Wildcard Mask: ",network.hostmask)
    print("Network Address: ",network.network_address)
    print('Broadcast Address: ',network.broadcast_address)
    print("Length of network prefix in bits: ",network.prefixlen)
    print("Total number of hosts under the network: ",network.num_addresses - 2)
    print("Usable Host Address Range in Network: ",res[0], "-", res[1])
    print("Total no of bits in the ip: ",ip.max_prefixlen)
    print('Total Number of Usable Networks in Parent Mask: ', len(list(network.subnets())))


    if more is True:
        print('Additional information displayed about the IP Address')
        print('View detailed explanations of the values listed below here: ')
        print('https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml')
        # Print True if the IP address is reserved for multicast use.
        print("Is multicast: ",ip.is_multicast)
        # Print True if the IP address is allocated for private networks.
        print("Is private: ",ip.is_private)
        # Print True if the IP address is global
        print("Is global: ",ip.is_global)
        # Print True if the IP address is unspecified.
        print("Is unspecified: ",ip.is_unspecified)
        # Print True if the IP address is otherwise IETF reserved.
        print("Is reversed: ",ip.is_reserved)
        # Print True if the IP address is a loopback address.
        print("Is loopback: ",ip.is_loopback)
        # Print True if the IP address is Link-local
        print("Is link-local: ",ip.is_link_local)
        # Print IP in Binary
        print('IP in Binary: ',MyIPv4(ip).binary_repr)
        # Print Netmask in Binary
        print('Netmask in Binary: ',MyIPv4(network.netmask).binary_repr)  # A /16 netmask

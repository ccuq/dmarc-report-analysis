import ipaddress
from dmarc_own import domain_name, spf_record

ip_lst = []

def spf_detail(spf_list):
    for spf_elem in spf_list:
        # print(spf_elem)
        if spf_elem.startswith('v=') or spf_elem.endswith('all'):
            continue
        elif spf_elem.startswith('ip4'):
            _select, _network = spf_elem.split(':')
            # print(_network)
            expand_ip(_network)
        elif spf_elem.startswith('ip6'):
            # _network = spf_elem.replace('ip6:', '')
            # print(_network)
            #expand_ip(_network)
            continue
        elif spf_elem.startswith('include'):
            _inc, _spf = spf_elem.split(':')
            # print(_spf)
            spf_detail([element for element in spf_record[_spf].split()])
        elif spf_elem.startswith('a'):
            _select, _network = spf_elem.split(':')
            # print(_network)
            expand_ip(spf_record[_network])
    return(ip_lst)


def expand_ip(spf_network):
    for network in spf_network.split():
        ip_lst.extend([str(host) for host in ipaddress.ip_network(network, strict=False).hosts()])
        # print(ip_lst)


def liste_ip():
    spf_detail([element for element in spf_record[domain_name].split()])
    return ip_lst

# my_ips = liste_ip()
# print(my_ips)
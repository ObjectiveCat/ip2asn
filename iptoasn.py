import sys

if sys.version_info[0] != 3 or sys.version_info[1] < 5:
    print("This script requires Python version 3.5")
    sys.exit(1)

import ipaddress
import subprocess


__author__ = "Vadim Petrov"
__email__ = "vadim@vadimpetrov.com"
__version__ = "0.1.0"
__license__ = "GPL"


def getasn(ipaddr):
    ptr = ipaddress.ip_address(ipaddr).reverse_pointer
    ptr_list = ptr.split('.')[:-2]
    final_ptr = '.'.join(ptr_list)
    if ipaddr.version is 4:
        subprocess.call(['dig', '+short', final_ptr + '.origin.asn.cymru.com', 'TXT'])
    if ipaddr.version is 6:
        subprocess.call(['dig', '+short', final_ptr + '.origin6.asn.cymru.com', 'TXT'])


getasn(ipaddress.ip_address(sys.argv[1]))
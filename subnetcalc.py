import typer

from ipaddress import IPv4Interface, AddressValueError
from helpers import validate_IPv4
from iplib import IPv4subnetted

app = typer.Typer()


print('\nInput valid IPv4 address or network with CIDR Notation.')
print('If not CIDR is given a /32 will be used as a host address.')
print('Example: 10.10.10.1/24')

#ipaddr = typer.Argument()

@app.command()
def subnetcalc(ipaddr: str, more: bool = False):
    print("*" * 100)
    print("*" * 100)
    print("*" * 100)
    validate_IPv4(ipaddr)
    ifc = IPv4Interface(ipaddr)
    IPv4subnetted(ifc,more)





if __name__=='__main__':
    app()
import re
from ipaddress import AddressValueError, IPv4Address, IPv4Interface
import time


class MyIPv4(IPv4Address):
    '''https://realpython.com/python-ipaddress-module
    referenced link above. 
    '''
    @property
    def binary_repr(self, sep=".") -> str:
        """Represent IPv4 as 4 blocks of 8 bits."""
        return sep.join(f"{i:08b}" for i in self.packed)

    @classmethod
    def from_binary_repr(cls, binary_repr: str):
        """Construct IPv4 from binary representation."""
        # Remove anything that's not a 0 or 1
        i = int(re.sub(r"[^01]", "", binary_repr), 2)
        return cls(i)


def get_input(prompt=''):
    try:
        line = input(prompt)
    except NameError:
        line = input(prompt)
    return line


def validate_IPv4(ipaddr: str):
    """Validates if entered argument is a valid IPv4 Address"""
    try:
        IPv4Interface(ipaddr)
        print('Valid IP Address entered!!: ', ipaddr)
        time.sleep(3)
        pass
    except AddressValueError as e:
        print('Invalid IP address has been entered.')
        print('The entered value was: ', ipaddr)
        print('Try running the script again with a valid address or network.')
        time.sleep(3)
        sys.exit()


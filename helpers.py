import re
from ipaddress import AddressValueError, IPv4Address, IPv4Interface


class MyIPv4(IPv4Address):
    """Extended IPv4Address class with binary representation capabilities."""
    
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


def validate_IPv4(ipaddr: str) -> bool:
    """
    Validates if entered argument is a valid IPv4 Address
    
    Args:
        ipaddr: String containing an IP address with optional CIDR notation
        
    Returns:
        bool: True if valid
        
    Raises:
        AddressValueError: If the IP address is invalid
    """
    try:
        IPv4Interface(ipaddr)
        return True
    except AddressValueError as e:
        raise AddressValueError(f"Invalid IP address: {ipaddr}. Please provide a valid IPv4 address with CIDR notation (e.g., 192.168.1.0/24)")

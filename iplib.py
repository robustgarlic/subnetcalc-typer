import ipaddress
from rich.table import Table
from rich.console import Console
from helpers import MyIPv4


console = Console()

class SubnetCalculator:
    """Class to handle subnet calculations and display formatting"""
    
    def __init__(self, interface: ipaddress.IPv4Interface):
        self.interface = interface
        self.network = interface.network
        self.hosts = list(self.network.hosts())
        self.first_host = self.hosts[0] if self.hosts else None
        self.last_host = self.hosts[-1] if self.hosts else None
    
    def create_subnet_table(self, show_binary: bool = False) -> Table:
        """
        Create a table with subnet information
        
        Args:
            show_binary: Whether to show binary representation of IP and netmask
            
        Returns:
            Table: Rich table object with subnet information
        """
        table = Table(title=f"Subnet Information for {self.interface}")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="green")
        
        # Basic subnet information
        table.add_row("IP Address", str(self.interface.ip))
        table.add_row("Subnet Mask", str(self.network.netmask))
        table.add_row("Network Address", str(self.network.network_address))
        table.add_row("Broadcast Address", str(self.network.broadcast_address))
        table.add_row("Prefix Length", str(self.network.prefixlen))
        table.add_row("Total Hosts", str(self.network.num_addresses - 2))
        if self.first_host and self.last_host:
            table.add_row("Usable Host Range", f"{self.first_host} - {self.last_host}")
        table.add_row("Total Networks", str(len(list(self.network.subnets()))))
        
        # Binary representation if requested
        if show_binary:
            table.add_row("IP Binary", MyIPv4(self.interface.ip).binary_repr)
            table.add_row("Netmask Binary", MyIPv4(self.network.netmask).binary_repr)
        
        return table
    
    def create_detailed_table(self) -> Table:
        """
        Create a table with detailed IP information
        
        Returns:
            Table: Rich table object with detailed IP information
        """
        detailed_table = Table(title="Additional IP Information")
        detailed_table.add_column("Property", style="cyan")
        detailed_table.add_column("Value", style="yellow")
        
        ip = self.interface.ip
        properties = [
            ("Is Multicast", ip.is_multicast),
            ("Is Private", ip.is_private),
            ("Is Global", ip.is_global),
            ("Is Reserved", ip.is_reserved),
            ("Is Loopback", ip.is_loopback),
            ("Is Link-local", ip.is_link_local)
        ]
        
        for prop, value in properties:
            detailed_table.add_row(prop, str(value))
        
        return detailed_table
    
    def display_subnet_info(self, detailed: bool = False, binary: bool = False):
        """
        Display subnet information in formatted tables
        
        Args:
            detailed: Whether to show detailed IP information
            binary: Whether to show binary representation
        """
        # Display main subnet information
        console.print(self.create_subnet_table(binary))
        
        # Display detailed information if requested
        if detailed:
            console.print("\n", self.create_detailed_table())


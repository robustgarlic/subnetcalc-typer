#!/usr/bin/env python3
import typer
from typing import Optional
from rich import print as rprint
from ipaddress import IPv4Interface, AddressValueError
from helpers import validate_IPv4
from iplib import SubnetCalculator

app = typer.Typer(
    help="A powerful subnet calculator CLI tool",
    add_completion=False,
)

def version_callback(value: bool):
    if value:
        rprint("[yellow]Subnet Calculator[/yellow] version 1.0.0")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=version_callback,
        is_eager=True,
    )
):
    """
    Calculate subnet information for IPv4 addresses.
    """
    pass

@app.command()
def calc(
    ipaddr: str = typer.Argument(..., help="IPv4 address with CIDR notation (e.g., 192.168.1.0/24)"),
    detailed: bool = typer.Option(
        False,
        "--detailed",
        "-d",
        help="Show detailed information about the IP address"
    ),
    binary: bool = typer.Option(
        False,
        "--binary",
        "-b",
        help="Show binary representation of IP and netmask"
    ),
):
    """
    Calculate subnet information for the given IPv4 address.
    
    Examples:
        subnetcalc calc 192.168.1.0/24
        subnetcalc calc 10.0.0.1/16 --detailed
        subnetcalc calc 172.16.0.0/12 --binary
    """
    try:
        validate_IPv4(ipaddr)
        ifc = IPv4Interface(ipaddr)
        
        # Create subnet calculator and display information
        calculator = SubnetCalculator(ifc)
        calculator.display_subnet_info(detailed=detailed, binary=binary)
        
    except (AddressValueError, ValueError) as e:
        rprint(f"[red]Error:[/red] {str(e)}")
        raise typer.Exit(1)
    except Exception as e:
        rprint(f"[red]An unexpected error occurred:[/red] {str(e)}")
        raise typer.Exit(1)

if __name__ == '__main__':
    app()
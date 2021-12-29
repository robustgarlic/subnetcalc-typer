# subnetcalc-typer
Silly simple subnet calculator using Typer and ipaddress


# subnet calculator
*Tested using Python 3.10.1*

This is a simple subnet calculator using the build in python library *[ipaddress](https://python.readthedocs.io/en/latest/library/ipaddress.html)* and the library
*[Typer](https://typer.tiangolo.com/)*.


# Usage

 1. `pip -r install requirements.txt`
 2.  example usage: `python subnetcalc.py 10.10.10.10/24` 
	 
	 **defaults to /32 subnet mask if none provided*
 3. add argument '-- more' to display additional information about the IPv4 Address.
	 
	 *example: `python subnetcalc.py 10.10.10.10/24 --more`

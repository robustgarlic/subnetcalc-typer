
# subnet calculator
*Tested using Python 3.10.1*

This is a silly simple subnet calculator using the build in python library *[ipaddress](https://python.readthedocs.io/en/latest/library/ipaddress.html)* and the library
*[Typer](https://typer.tiangolo.com/)*.


# Usage

 1. git clone https://github.com/robustgarlic/subnetcalc-typer.git
 2. `pip -r install requirements.txt`
 3.  example usage: `python subnetcalc.py 10.10.10.10/24` 
 
	 -*defaults to /32 subnet mask if none provided*
 5. add argument '-- more' to display additional information about the IPv4 Address.
	 
	 -example: `python subnetcalc.py 10.10.10.10/24 --more`



**To Do**
 - [ ] Ipv6.
 - [ ] Incorporate the Library [Rich](https://github.com/willmcgugan/rich) and its features.
 - [ ] Better output formatting
 - [ ] Better Comments

# Subnet Calculator

A powerful command-line subnet calculator built with Python and Typer.

## Features

- Calculate subnet information for IPv4 addresses
- Display detailed IP address information
- Show binary representation of IP and netmask
- Beautiful command-line interface with colored output
- Easy to use with intuitive commands

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/subnetcalc-typer.git
cd subnetcalc-typer
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic subnet calculation:
```bash
python subnetcalc.py calc 192.168.1.0/24
```

Show detailed information:
```bash
python subnetcalc.py calc 10.0.0.1/16 --detailed
```

Show binary representation:
```bash
python subnetcalc.py calc 172.16.0.0/12 --binary
```

Show version:
```bash
python subnetcalc.py --version
```

Get help:
```bash
python subnetcalc.py --help
python subnetcalc.py calc --help
```

## License

MIT License

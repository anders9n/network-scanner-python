================================================================================
                  Basic Python Network Audit Tool v1.0
================================================================================

DESCRIPTION
-----------
A Python script that displays common network ports and allows you to verify
if they are open or closed on a specific host. This tool performs basic TCP
port scanning capabilities for network auditing purposes.

The project demonstrates concepts from CS50P Week 2:
- Lists
- For loops
- Functions

REQUIREMENTS
-----------
- Python 3.x
- socket module (included in Python standard library)
- sys module (included in Python standard library)
- colorama module (optional, for colored output)
  - On Debian/Kali systems: python3-colorama

INSTALLATION
------------
The script requires no additional installation if colorama is already installed
on your system. If you need to install colorama:

On Debian/Kali systems:
    sudo apt install python3-colorama

Or using pip (in a virtual environment):
    pip install colorama

USAGE
-----
Basic execution (tests on localhost):
    python3 puertos_ciberseguridad.py

Execution with a specific host (via command line argument):
    python3 puertos_ciberseguridad.py 192.168.1.10
    python3 puertos_ciberseguridad.py example.com

Interactive mode:
    python3 puertos_ciberseguridad.py
    # The script will prompt you to enter the host to scan

MAIN FUNCTIONS
--------------
1. mostrar_puertos(lista_puertos)
   - Displays a list of ports in a readable format
   - Uses a for loop to iterate over the list
   - Shows total count of ports

2. puerto_abierto(host, puerto, timeout=0.5)
   - Attempts to connect to a TCP port on a specific host
   - Returns True if the port is open, False if closed/filtered
   - Default timeout: 0.5 seconds
   - Uses socket.connect_ex() for connection testing

3. mostrar_estado_puertos(host, lista_puertos)
   - Verifies the status of multiple ports on a host
   - Displays results with colors (green for open, red for closed)
   - Works without colorama if not available (falls back to plain text)
   - Provides clear visual feedback for port status

4. main()
   - Main function that orchestrates program execution
   - Defines the port range to scan (ports 1-1024 by default)
   - Handles command line arguments and interactive input
   - Initializes colorama if available

PORT RANGE
----------
The script scans ports from 1 to 1024 (well-known ports) by default.
This includes common services such as:

    22    - SSH (Secure Shell)
    23    - Telnet
    25    - SMTP (Simple Mail Transfer Protocol)
    53    - DNS (Domain Name System)
    80    - HTTP (HyperText Transfer Protocol)
    161   - SNMP (Simple Network Management Protocol)
    443   - HTTPS (HTTP Secure)

FEATURES
--------
✓ Colored Output
  - Green highlighting for open ports
  - Red highlighting for closed ports
  - Automatic color reset after each print
  - Graceful fallback to plain text if colorama is unavailable

✓ Robust Error Handling
  - Safe import of optional dependencies
  - Try/except blocks for graceful degradation
  - Timeout configuration to prevent hanging connections

✓ Flexible Host Input
  - Command line argument support (sys.argv)
  - Interactive input mode for user-friendly operation
  - Default fallback to localhost (127.0.0.1)

✓ Efficient Port Scanning
  - TCP connection-based port detection
  - Configurable timeout values
  - Context managers for proper resource cleanup
  - Non-blocking socket operations

✓ Educational Code Structure
  - Well-documented functions with docstrings
  - Clear variable naming
  - Modular design following CS50P principles
  - Comments explaining programming concepts

✓ Cross-Platform Compatibility
  - Works on Linux, Windows, and macOS
  - Standard library dependencies only (except colorama)
  - No external network tools required

OUTPUT EXAMPLES
---------------
Port List Display:
--------------------------------------------------
Do you want to see which ports are open?
--------------------------------------------------
Port 1
Port 2
Port 3
...
Port 1024
--------------------------------------------------
Total ports: 1024

Port Status Check:
--------------------------------------------------
Scanning ports on 192.168.1.10 (TCP):
--------------------------------------------------
Port 22: OPEN
Port 23: CLOSED
Port 25: CLOSED
Port 80: OPEN
Port 443: OPEN
...
--------------------------------------------------

IMPORTANT NOTES
---------------
- The script uses TCP connections to verify ports
- Short timeouts may produce false negatives on slow connections
- Only verifies if the port accepts connections, does not identify the service
- This tool should be used ethically and legally
- Do not scan hosts without proper authorization
- Scanning large port ranges may take significant time
- Some firewalls may block or filter port scan attempts

PROGRAMMING CONCEPTS USED
--------------------------
- Lists: Storage of multiple port numbers
- For loops: Iteration over list elements
- Functions: Modular code organization
- Exception handling: Try/except for optional imports
- Command line arguments: sys.argv processing
- Sockets: Low-level network communication
- Context managers: Resource management with 'with' statements
- Input/Output: User interaction and formatted printing
- Conditional statements: Control flow based on port status
- String formatting: f-strings for dynamic output

TECHNICAL DETAILS
-----------------
- Protocol: TCP (SOCK_STREAM)
- Connection method: socket.connect_ex()
- Default timeout: 0.5 seconds per port
- Port range: 1-1024 (well-known ports)
- Color library: colorama (optional)
- Python version: 3.x compatible

AUTHOR
------
Educational project based on CS50P - Week 2

LICENSE
-------
Educational use only - For learning purposes

VERSION
-------
v1.0

================================================================================
                            END OF DOCUMENTATION
================================================================================

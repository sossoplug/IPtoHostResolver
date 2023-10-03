import socket
import os
import datetime
from typing import List, Optional

# ==================
# Load IP Adress
# ==================
def load_ip_addresses(filepath: str) -> List[str]:
    """
    Load IP addresses from the specified file.

    Args:
    - filepath (str):       Path to the file containing IP addresses.

    Returns:
    - List[str]:            List of IP addresses.
    """
    try:
        with open(filepath, "r") as file:
            ip_addresses    = [ip.strip() for ip in file.readlines()]
        return ip_addresses
    except Exception as e:
        write_to_log(f"Failed to load IP addresses from {filepath}: {str(e)}", "ERROR")
        return []

# ==================
# Resolve Hostname
# ==================
def resolve_hostname(ip_address: str) -> Optional[str]:
    """
    Resolve the hostname for a given IP address.

    Args:
    - ip_address (str):     The IP address to resolve.

    Returns:
    - Optional[str]:        The resolved hostname or None if resolution fails.
    """
    try:
        hostname, _, _      = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror as e:
        write_to_log(f"Unable to resolve IP {ip_address}: {str(e)}", "ERROR")
        return None

# ==================
# Write Hostname to file
# ==================
def write_hostname_to_file(filepath: str, hostname: str) -> None:
    """
    Write/appends a resolved hostname to the specified file.

    Args:
    - filepath (str):   Path to the output file.
    - hostname (str):   The hostname to write to the file.

    Returns:
    - None
    """
    try:
        with open(filepath, "a") as file:
            file.write(f"https://{hostname}\n")
    except Exception as e:
        write_to_log(f"Failed to write hostname {hostname} to {filepath}: {str(e)}", "ERROR")

# ==================
# Write to Log
# ==================
def write_to_log(message: str, status: str) -> None:
    """
    Write a message to the specified log file.

    Args:
    - message (str):    The message to be logged.
    - status (str):     The status of the message (ERROR/SUCCESS).

    Returns:
    - None
    """
    try:
        timestamp       = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(os.getenv("LOG_OUTPUT_FILEPATH"), "a") as log_file:
            log_file.write(f"[{timestamp}] INFO: [{status}]: {message}\n")

        print(message)

    except Exception as e:
        print(f"[ERROR]: Failed to write to log. {str(e)}")

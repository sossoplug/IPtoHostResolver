import socket
import os
import datetime
from typing import List, Optional
import subprocess

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
# Ping Domain
# ==================
def is_domain_active(hostname: str, timeout: int = 1) -> bool:
    """
    Check if a domain is active by pinging it.

    Args:
    - hostname (str):   The domain to ping.
    - timeout (int):    The timeout for the ping in seconds. Default is 1 second.

    Returns:
    - bool:             True if the domain is active, False otherwise.
    """
    try:

        subprocess.check_output(["ping", "-c", "1", "-W", str(timeout), hostname])  # Trying to ping the domain
        return True
    except subprocess.CalledProcessError:
        # Logging and returning False if ping fails
        write_to_log(f"Domain {hostname} is not active.", "INFO")
        return False
    except Exception as e:
        # Logging any unexpected error
        write_to_log(f"Failed to ping {hostname}: {str(e)}", "INFO")
        return False


# ==================
# Write Hostname to file
# ==================
def write_hostname_to_file(filepath: str, hostname: str) -> None:
    """
    Write/appends a resolved hostname to the specified file if the domain is active.

    Args:
    - filepath (str):   Path to the output file.
    - hostname (str):   The hostname to write to the file.

    Returns:
    - None
    """
    try:
        if is_domain_active(hostname):
            with open(filepath, "a") as file:
                file.write(f"https://{hostname}\n")
        else:
            write_to_log(f"Hostname {hostname} was not written to the file as it is not active.", "INFO")
    except Exception as e:
        write_to_log(f"Failed to write hostname {hostname} to {filepath}: {str(e)}", "FAIL")


# ==================
# Post-Process Output File
# ==================
def post_process_output_file(filepath: str) -> None:
    """
    Perform post-processing on the output file to refine the final output.
    This function removes duplicate entries and sorts the domains alphabetically.

    Args:
    - filepath (str):       Path to the output file.

    Returns:
    - None
    """
    try:

        with open(filepath, "r") as file:                                       # Read the file and perform post-processing
            unique_domains  = set(file.readlines())                             # Reading all lines and removing duplicates by converting to a set


        sorted_domains      = sorted(unique_domains, key=lambda x: x.lower())   # Sorting the domains alphabetically


        with open(filepath, "w") as file:                                       # Writing back the refined data to the file
            file.writelines(sorted_domains)

        write_to_log(f"Post-processed {filepath}: removed duplicates and sorted entries.", "INFO")
    except Exception as e:
        # Logging any unexpected error
        write_to_log(f"Failed to post-process {filepath}: {str(e)}", "FAIL")


# ==================
# Write to Log
# ==================
def write_to_log(message: str, status: str) -> None:
    """
    Write a message to the specified log file.

    Args:
    - message (str):    The message to be logged.
    - status (str):     The status of the message (ERROR/SUCCESS/FAIL/INFO).

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


# ===================
#  Wipe Clean a file
# ===================
def wipe_file_clean(file_path):
    """
    Wipe clean a file
    - file_path (str):   Path to the file containing SMTP details.
    Returns:             None.
    """
    try:
        with open(file_path, 'w') as file:
            pass

        print(f"File '{file_path}' has been wiped clean.")

    except Exception as e:
        print(f"An error occurred while wiping the file '{file_path}': {e}")

from typing import List
from utils import  resolve_hostname, write_hostname_to_file, write_to_log


# ==================
# Resolve IP Addresses in Thread
# ==================
def resolve_ip_addresses_in_thread(ip_addresses: List[str], output_filepath: str, log_filepath: str) -> None:
    """
    Resolve hostnames for a list of IP addresses in a separate thread and writes any resolved hostnames to the output file, and logs using the specified log file.

    Args:
    - ip_addresses (List[str]):     List of IP addresses to resolve.
    - output_filepath (str):        Path to the file where found hostnames will be written.
    - log_filepath (str):           Path to the log file.

    Returns:
    - None
    """
    try:
        i                           = 0
        for ip in ip_addresses:
            hostname                = resolve_hostname(ip)

            i                       += 1

            if hostname:
                write_hostname_to_file(output_filepath, hostname)
                write_to_log(f"======================================================================" ,"")
                write_to_log(f"[#{i}] Resolved {ip} to {hostname}", "INFO")
            else:
                write_to_log(f"======================================================================", "")
                write_to_log(f"[#{i}] Failed to resolve {ip}", "INFO")

    except Exception as e:
        write_to_log(f"Error in thread: {str(e)}", "FAIL")



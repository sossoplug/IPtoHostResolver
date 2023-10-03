import os
import threading

from ip_resolver import resolve_ip_addresses_in_thread
from utils import load_ip_addresses, write_to_log, post_process_output_file, wipe_file_clean
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())


# ==================
# Main Function
# ==================
def main():
    """
    Coordinates the overall process of reading IP addresses, spawning threads, and writing resolved hostnames to the output file.

    Returns:
    - None
    """
    try:

        # Load environment variables
        ip_list_filepath            = os.getenv("IP_LIST_FILEPATH")
        number_of_threads           = int(os.getenv("NUMBER_OF_THREADS"))
        found_urls_filepath         = os.getenv("FOUND_URLS_FILEPATH")
        log_output_filepath         = os.getenv("LOG_OUTPUT_FILEPATH")

        # Cleaned files
        wipe_file_clean(log_output_filepath)
        wipe_file_clean(found_urls_filepath)

        # Load IP addresses
        ip_addresses                = load_ip_addresses(ip_list_filepath)

        # Divide IP addresses among threads
        ips_per_thread              = len(ip_addresses) // number_of_threads
        threads                     = []

        for i in range(number_of_threads):
            start_index             = i * ips_per_thread
            end_index               = (i + 1) * ips_per_thread if i != number_of_threads - 1 else None
            thread_ips              = ip_addresses[start_index:end_index]

            # Create and start thread
            t                       = threading.Thread(target=resolve_ip_addresses_in_thread, args=(thread_ips, found_urls_filepath, log_output_filepath))
            threads.append(t)
            t.start()

        # Wait for all threads to finish
        for t in threads:
            t.join()

        # After all threads have completed, perform post-processing on the output file
        post_process_output_file(os.getenv("FOUND_URLS_FILEPATH"))

    except Exception as e:
        write_to_log(f"Error in main function: {str(e)}", "ERROR")
    else:
        write_to_log("Hostname resolution completed successfully.", "SUCCESS")

if __name__ == "__main__":
    main()
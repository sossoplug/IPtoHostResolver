# IPToHostResolver

## Description
IPToHostResolver is a Python script designed to resolve IP addresses to their respective hostnames. Utilizing multithreading, the script efficiently processes multiple IP addresses concurrently, providing a fast and reliable way to obtain hostnames, which are then logged to an output file.

## Features
- **Multithreading**: Efficiently resolves multiple IP addresses concurrently.
- **Hostname Resolution**: Converts IP addresses to their respective hostnames.
- **Logging**: Keeps a detailed log of the resolution process and any errors encountered.
- **Configurability**: Allows customization via environment variables.

## Prerequisites
- Python 3.x
- Additional Python packages: `python-dotenv` (Install using `pip install python-dotenv`)

## Configuration
Configure the script using the `.env` file. Define the following variables:
- `IP_LIST_FILEPATH`: Path to the file containing the IP addresses to resolve.
- `NUMBER_OF_THREADS`: Number of threads to use for concurrent resolution.
- `FOUND_URLS_FILEPATH`: Path to the file where resolved hostnames will be written.
- `LOG_OUTPUT_FILEPATH`: Path to the log file.

## Usage
1. Populate the `.env` file with the appropriate variable values.
2. Ensure the IP address file specified in `IP_LIST_FILEPATH` is populated with IP addresses, one per line.
3. **Setting Up a Virtual Environment**:
   - Create a virtual environment: `python -m venv venv`
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On macOS and Linux: `source venv/bin/activate`

4. **Install Dependencies**:
   - Install the required packages: `pip install -r requirements.txt`
5. Run the script using `python main.py`.
6. Review the resolved hostnames in the file specified in `FOUND_URLS_FILEPATH` and check `LOG_OUTPUT_FILEPATH` for logs.

## Output
- **Resolved Hostnames**: Found hostnames are written line by line to the file specified in `FOUND_URLS_FILEPATH`.
- **Logs**: Detailed logs of the resolution process, including any errors, are written to `LOG_OUTPUT_FILEPATH`.

## Ethical Use
Please utilize IPToHostResolver ethically and responsibly. Ensure that your usage complies with local laws and regulations, and respect the privacy and rights of others.

## Contribution
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
[Specify License]


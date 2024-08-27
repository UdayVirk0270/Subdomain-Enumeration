import requests
from bs4 import BeautifulSoup
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function for scanning subdomains
def domain_scanner(domain_name, sub_domnames, threads, include_sc, include_loc, include_title):
    print('----URL after scanning subdomains----')

    def scan_subdomain(subdomain):
        url = f"https://{subdomain}.{domain_name}"
        subdomain_info = {'url': url}

        try:
            response = requests.get(url, timeout=5)
            subdomain_info['status_code'] = response.status_code if include_sc else None
            subdomain_info['location'] = response.headers.get('Location', 'N/A') if include_loc else None
            
            if include_title:
                soup = BeautifulSoup(response.text, 'html.parser')
                subdomain_info['title'] = soup.title.string.strip() if soup.title else 'N/A'
            print_subdomain_info(subdomain_info)
            return subdomain_info
            
        except requests.ConnectionError:
            pass
        except requests.Timeout:
            subdomain_info['status_code'] = 'Timeout'
            print_subdomain_info(subdomain_info)
            return subdomain_info

    def print_subdomain_info(info):
        line = f"[+] {info['url']}"
        if info['status_code'] is not None:
            line += f" - Status Code: {Fore.RED}{info['status_code']}{Style.RESET_ALL}"
        if info.get('location'):
            line += f" - Location: {Fore.GREEN}{info['location']}{Style.RESET_ALL}"
        if info.get('title'):
            line += f" - Title: {Fore.YELLOW}{info['title']}{Style.RESET_ALL}"
        print(line)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(scan_subdomain, sub) for sub in sub_domnames]
        for future in as_completed(futures):
            future.result()

# Main function
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Subdomain Scanner")
    parser.add_argument('domain', help="The domain to scan subdomains for")
    parser.add_argument('-T', '--threads', type=int, default=10, help="Number of threads to use")
    parser.add_argument('-sc', '--status-code', action='store_true', help="Include status code of subdomains (Red)")
    parser.add_argument('-l', '--location', action='store_true', help="Include redirection location of subdomains (Green)")
    parser.add_argument('-t', '--title', action='store_true', help="Include title of the subdomains (Yellow)")
    parser.add_argument('-f', '--file', type=str, default='subdomain_names1.txt', help="File containing subdomain names")
    args = parser.parse_args()

    # Opening the subdomain text file
    with open(args.file, 'r') as file:
        sub_dom = file.read().splitlines()

    # Calling the function for scanning the subdomains and getting the URL
    domain_scanner(args.domain, sub_dom, args.threads, args.status_code, args.location, args.title)

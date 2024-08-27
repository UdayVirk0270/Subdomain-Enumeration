---

# Subdomain Enumeration Tool

This is a Python-based tool for enumerating subdomains of a given domain. The tool supports multithreading for faster enumeration and can provide additional details like HTTP status codes, redirection locations, and page titles.

## Features

- **Multithreading**: Scan multiple subdomains concurrently using threads to speed up the process.
- **Status Codes**: Retrieve and display the HTTP status code for each subdomain.
- **Redirection Location**: Display the redirection location if the subdomain redirects to another URL.
- **Page Titles**: Extract and display the page title of each subdomain.

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/subdomain-enumeration-tool.git
cd subdomain-enumeration-tool
```

Install the required Python packages:

```pip install -r requirements.txt
```

## Usage

```bash
python subdomain_enum.py <domain> [options]
```

### Options
![Screenshot 2024-08-27 234234](https://github.com/user-attachments/assets/9597eeb6-530d-40a5-8c32-72cff5a26264)

- `-T, --threads <number>`: Number of threads to use for concurrent requests (default is 10).
- `-sc, --status-code`: Include HTTP status codes in the output (displayed in red).
- `-l, --location`: Include redirection locations in the output (displayed in green).
- `-t, --title`: Include page titles in the output (displayed in yellow).
- `-f, --file <filename>`: Specify a file containing subdomains to scan (default is `subdomain_names1.txt`).

### Example

```
python subdomain_enum.py example.com -T 20 -sc -l -t -f subdomain_names1.txt
```

### Sample Output
![Screenshot 2024-08-27 234332](https://github.com/user-attachments/assets/1a81a82d-d6e4-440c-bb8a-7db634cfb5e8)

```
----URL after scanning subdomains----
[+] https://www.example.com - Status Code: 200 - Title: Example Domain
[+] https://mail.example.com - Status Code: 301 - Location: https://mail2.example.com - Title: Mail Redirect
[+] https://admin.example.com - Status Code: 403
```

## Subdomain List

The tool uses a list of common subdomains provided in a text file. You can customize this list by editing or replacing the default file (`subdomain_names1.txt`).

## Contributing

Feel free to fork this repository, submit pull requests, or open issues for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Replace `yourusername` with your actual GitHub username and make sure to add the necessary files (`requirements.txt`, etc.) to your repository before pushing. This `README.md` file should provide clear instructions for users on how to use and contribute to your project.

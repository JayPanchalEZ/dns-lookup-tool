# DNS Lookup Tool
A Python script to fetch and display DNS records (A, CNAME, MX) for a given domain. This project is beginner-friendly, built to showcase basic networking and Python scripting skills.

---

## 🌟 Features
- Retrieves **A records** (IP addresses).
- Retrieves **CNAME records** (canonical names).
- Retrieves **MX records** (mail servers).
- Validates user input to ensure the domain format is correct.
- Handles errors gracefully (e.g., non-existent domains or no DNS records).

---

## 🛠️ Prerequisites
Before running the script, ensure you have:
- Python 3.6 or higher installed on your system.
- The `dnspython` library installed.

To install the library, run:
```bash
pip install dnspython
```

---

## 🚀 How to Run
1. **Clone this Repository**:
   ```bash
   git clone https://github.com/JayPanchalEZ/dns-lookup-tool.git
   cd dns-lookup-tool
   ```

2. **Navigate to the `src` Folder**:
   ```bash
   cd src
   ```

3. **Run the Script**:
   ```bash
   python dns_lookup.py
   ```
   or you can directly go to the src folder using GUI and open dnslookup.bat file.

4. **Follow the Prompt**:
   - Enter a valid domain name when prompted (e.g., `example.com`).

---

## 🔍 Example Usage
### Input:
```text
Enter a domain name (e.g., example.com): google.com
```

### Output:
```text
DNS Records for google.com:

A Records (IP Addresses):
 - 142.250.182.206

CNAME Records:
 - No CNAME records found.

MX Records (Mail Servers):
 - alt4.gmail-smtp-in.l.google.com (Priority: 40)
```

---

## ⚠️ Error Handling
- **Invalid Input**: If the domain format is invalid, the script prompts the user to re-enter a valid domain.
  Example:
  ```text
  Enter a domain name (e.g., example.com): asdhfsaf
  Invalid domain format. Please enter a valid domain (e.g., example.com).
  ```
- **Non-Existent Domain**: If the domain does not exist, the script displays a message.
  Example:
  ```text
  DNS Records for invalid-domain.com:

  A Records (IP Addresses):
   - Domain does not exist.
  ```

---

## 💂🏻‍♂️ Project Structure
```
dns-lookup-tool/
├── src/
│   ├── dns_lookup.py     # The main script
│   └── dnslookup.bat     # Batch file to run the script in Command Prompt
└── README.md             # Project documentation
```

---

## 📚 Concepts Covered
This project demonstrates:
- **DNS Basics**:
  - A records, CNAME records, and MX records.
- **Python Basics**:
  - Input validation.
  - Error handling with `try` and `except`.
- **Regular Expressions**:
  - Validating domain name formats.
- **Networking Knowledge**:
  - Understanding DNS queries and their use in cybersecurity.

---

## 💡 Ideas for Enhancement
- Add more record types (e.g., TXT, NS, SOA).
- Create a web-based version using Flask or Django.
- Include a feature to save results to a text or CSV file.
- Automate DNS lookups for multiple domains in bulk.

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit pull requests.

---

## 👤 Author
**Jay Panchal**

- [GitHub](https://github.com/JayPanchalEZ)
- [LinkedIn](https://www.linkedin.com/in/jaypanchal634)

---

## 🌐 Acknowledgments
- **[TryHackMe](https://tryhackme.com/)** for inspiring this project through the Presecurity path.
- The [dnspython](https://www.dnspython.org/) library for making DNS queries simple.


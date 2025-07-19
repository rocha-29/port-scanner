# 🔍 Port Scanner

A simple and multithreaded Python-based port scanner built by **D_R0x** as part of my cybersecurity portfolio.

## 📌 Overview

This script scans a range of ports on a given host (IP or domain) to check which ports are open. It uses **sockets**, **threads**, and **input validation** to ensure efficient and reliable scanning. Results are saved to a text file automatically.

## ⚙️ Features

- Multi-threaded port scanning
- Customizable port range
- Input validation (host and port range)
- Saves results to a `.txt` file
- Educational and beginner-friendly
- Command-line interface using `argparse`
- Cool ASCII banner on launch 😎

## 🚀 Usage

### 🖥️ Run from terminal

```bash
python port_scanner.py <target_host> -p <port_range>


📚 Examples
Scan ports from 1 to 1024 on a domain:

python port_scanner.py scanme.nmap.org

Scan a specific port range on an IP address:

python port_scanner.py 192.168.0.1 -p 20-80

💾 Output
If open ports are found, the results will be saved to a file named:

<target_host>_open_ports.txt

Example content:

Port 22 is open
Port 80 is open
Port 443 is open


⚠️ Disclaimer
This script is for educational purposes only. Always have explicit permission before scanning any system.

🧠 Author
Daniel Rocha (D_R0x)
Cybersecurity student.

⭐️ If you find this helpful, consider giving the repo a star!
# Python Multi‑Threaded Network Scanner

A high‑performance, multi‑threaded network scanner built in Python.  
Created as part of my journey as a **Microsoft Learn Student Ambassador**, this project demonstrates practical cybersecurity fundamentals, Python automation, and systems‑level problem solving.

---

## 🎓 Why I Built This (Ambassador Purpose)

As a Student Ambassador, I focus on helping students understand real‑world cybersecurity concepts through hands‑on tools.  
This scanner is designed to:

- teach networking fundamentals  
- demonstrate Python threading  
- show how port scanning works  
- give students a safe way to explore their own networks  
- inspire beginners to build their own security tools  

This project is part of my mission to empower students with accessible, practical cybersecurity knowledge.

---

## ✨ Features

- ⚡ Multi‑threaded host discovery  
- 🔍 Fast TCP port scanning  
- 📊 Clean, sorted output  
- 🧩 Customizable port list  
- 🖥️ Works on Windows, Linux, and macOS  
- 🧠 Beginner‑friendly code structure for teaching  

 

## 📌 Example Output

```text
192.168.1.1 is online
    53 is open
    80 is open

192.168.1.37 is online
    135 is open
    139 is open
    445 is open
    3389 is open
```
## 🚀 How to Run

### 1. Install Python 3.10+
Make sure Python is installed and added to your PATH.

### 2. Install dependencies
This project only needs `tqdm`:

```bash
pip install tqdm
```
## 3. Find your network prefix (IMPORTANT)
your network may not be 192.168.1.x

Windows
Run:
```bash
ipconfig
```
Look for your IPv4 address, for example
```code
IPv4 Address .....: 192.168.0.24
```
Your network prefix is everything except for the last number:
```code
192.168.0
```
macOS/Linux
Run:
```bash
ip a
```
Look for something like 
```code
inet 10.0.0.52/24
```
Your network prefix is 
```code
10.0.0
```
### 4. Run the scanner using your prefix
```bash
python Network Scanner.py -n <your_prefix_here>
```
Examples
```bash
python network_scanner.py -n 192.168.0
python network_scanner.py -n 10.0.0
python network_scanner.py -n 172.16.5
```
Optional: Scan custom ports
```bash
python Network Scanner.py -n 192.168.1 -p 22,80,443
```
## 🖥️ macOS Support

This scanner works on macOS without any changes.
- Use python3 instead of python
- Use ifconfig or ip a to find your network prefix
- All arguments (-n, -p, --network, --ports) work exactly the same
Example:
```bash
python3 network_scanner.py -n 10.0.0
```
## 🛠 Command Line Options

| Flag | Description | Example |
| :--- | :--- | :--- |
| `-n` / `--network` | Network prefix to scan | `-n 192.168.1` |
| `-p` / `--ports` | Custom comma-separated ports | `-p 22,80,443` |

## 📚 Learning Outcomes (Microsoft Student Ambassador Focus)
Students who explore this project will learn:
- How ICMP ping works
- How TCP ports and services operate
- How Python sockets function
- How threading accelerates network tasks
- How to structure a real security tool
- How to interpret scan results responsibly

## 💡 Future Improvements
- Planned upgrades include:
- UDP scanning
- OS fingerprinting
- Service banner grabbing
- MAC vendor lookup
- JSON/CSV export
- Azure‑hosted dashboard
- AI‑powered vulnerability hints

## 👤 Author
Tyler Bones 
Microsoft Learn Student Ambassador

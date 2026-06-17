Python Multi‑Threaded Network Scanner
A high‑performance, multi‑threaded network scanner built in Python.
Created as part of my journey as a Microsoft Learn Student Ambassador, this project demonstrates practical cybersecurity fundamentals, Python automation, and systems‑level problem solving.

🎓 Why I Built This (Ambassador Purpose)
As a Student Ambassador, I focus on helping students understand real‑world cybersecurity concepts through hands‑on tools.
This scanner is designed to:

teach networking fundamentals

demonstrate Python threading

show how port scanning works

give students a safe way to explore their own networks

inspire beginners to build their own security tools

This project is part of my mission to empower students with accessible, practical cybersecurity knowledge.

✨ Features
⚡ Multi‑threaded host discovery

🔍 Fast TCP port scanning

📊 Clean, sorted output

🧩 Customizable port list

🖥️ Works on Windows, Linux, and macOS

🧠 Beginner‑friendly code structure for teaching

📌 Example Output
Code
192.168.1.1 is online
    53 is open
    80 is open

192.168.1.37 is online
    135 is open
    139 is open
    445 is open
    3389 is open
🚀 How to Run
Install Python 3.10+

Install tqdm:

Code
pip install tqdm
Run the scanner:

Code
python network_scanner.py -n 192.168.1
🛠️ Command Line Options
Flag	Description	Example
-n / --network	Network prefix to scan	-n 192.168.1
-p / --ports	Custom comma‑separated ports	-p 22,80,443


📚 Learning Outcomes (Ambassador Focus)
Students who explore this project will learn:

how ICMP ping works

how TCP ports and services operate

how Python sockets function

how threading accelerates network tasks

how to structure a real security tool

how to interpret scan results responsibly

This makes it a great demo for workshops, clubs, and Ambassador events.

💡 Future Improvements
Planned upgrades include:

UDP scanning

OS fingerprinting

Service banner grabbing

MAC vendor lookup

JSON/CSV export

Azure‑hosted dashboard

AI‑powered vulnerability hints

These improvements will help expand the educational impact of the project.

👤 Author
Tyler Bones
Microsoft Learn Student Ambassador
Focused on cybersecurity, Python automation, and AI‑enhanced tooling.

import subprocess
import threading
from tqdm import tqdm 
import time
import socket
import argparse
results = {}
thread_limiter = threading.Semaphore(200)
parser = argparse.ArgumentParser(description="Multi-threaded Network Scanner")

parser.add_argument(
   "-n", "--network",
   required = True,
   help ="Network Prefix to scan (example: 192.168.1)"
)

parser.add_argument(
    "-p", "--ports",
    help="Comma-separated list of ports to scan (default: common ports)",
    default=None    
    )
args = parser.parse_args()
network = args.network
def scan_port(ip, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(0.2)
  result = s.connect_ex((ip, port))
  s.close()
  return result == 0

def port_worker(ip, port):
    with thread_limiter:
        try:
            if scan_port(ip, port):
                results[ip].append(port)
        finally:
            pass


def ping(ip):
    with thread_limiter:
        result = subprocess.run(["ping", "-n", "1", ip], stdout=subprocess.DEVNULL)
        if result.returncode == 0:

            common_ports = [
                20, 21, 22, 23, 25, 53, 67, 68, 69, 80,
                110, 111, 123, 135, 137, 138, 139,
                143, 161, 162, 389, 443, 445, 465,
                514, 520, 587, 631, 636, 873, 902,
                989, 990, 993, 995, 1080, 1194, 1433,
                1521, 1723, 3128, 3268, 3306, 3389,
                4444, 4500, 5000, 5060, 5432, 5500,
                5631, 5900, 5985, 5986, 6379, 6667,
                7001, 8000, 8080, 8081, 8443, 8888,
                9000, 9090, 9200, 9418, 9999
            ]

            results[ip] = []      # create entry for this IP
            port_threads = []

            def port_task(port):
                if scan_port(ip, port):
                    results[ip].append(port)

            for port in common_ports:
                t = threading.Thread(target=port_task, args=(port,))
                t.start()
                port_threads.append(t)

            for t in port_threads:
                t.join()

            results[ip] = sorted(results[ip])


start = time.time()

threads = []

for host in tqdm(range(1, 255), desc="Scanning"):
  ip = f"{network}.{host}"
  t = threading.Thread(target=ping, args=(ip,))
  t.start()
  threads.append(t)

for t in threads:
  t.join()

end = time.time()
print(f"\nScan completed in {end - start:.2f} seconds")

for ip in sorted(results, key=lambda x: list(map(int, x.split('.')))):
    print(f"{ip} is online")
    for port in results[ip]:
        print(f"    {ip}:{port} is open")

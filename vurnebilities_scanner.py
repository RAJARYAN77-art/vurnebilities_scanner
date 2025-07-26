import argparse
import subprocess
import re

def scan_ports(target):
    print(f"[+]scanning {target} for open ports and service version...\n")
    try:
        result=subprocess.check_output(['nmap' , '-sV' , 'T4', target],text= True)
    except subprocess.CalledProcessError as e:
        print(f"[-]scan failed :{e}")
        return
    
    print("[*]scan Results:\n")
    print(result)

    print("\n[*]summary of open ports and services:")
    for line in result.split('\n'):
        if re.match(r'^\d+/tcp\s+open' , line):
            print(" " + line.strip())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="port & Service Version Scanner using Nmap")
    parser.add_argument("target", help="Target IP address or domain")
    args = parser.parse_args()
    
    scan_ports(args.target)
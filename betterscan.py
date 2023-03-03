import os
import subprocess
# Just a simple script to automate scan and enumeration 
# Made by: SparQz

# Get IP address from user
ip_address = input("Enter the IP address to scan: \n")

# Get type of Nmap scan to run from user

scan_type = input("Enter the type of Nmap scan to run(quiet/aggressive/intensive): ")

print ("-----Running Nmap scan-----\n")
# Run Nmap scan
if scan_type == "quiet":
    nmap_command = f"nmap -sV -Pn {ip_address} -oN {ip_address}_nmap.txt"
elif scan_type == "aggressive":
    nmap_command = f"nmap -A {ip_address} -oN {ip_address}_nmap.txt"
elif scan_type == "intensive":
    nmap_command = f"nmap -sC -sV -A -T4 -v {ip_address} -oN {ip_address}_nmap.txt"
else:
    print("Invalid scan type")
    exit()

os.system(nmap_command)
# Find wordlist for gobuster and export location to shell
directory_name = 'Web-Content'
file_name = 'directory-list-2.3-big.txt'
file_path = os.path.abspath(os.path.join(directory_name, file_name))

subprocess.run(f'export DIRBIG="{file_path}"', shell=True)


gobuster_type = input("Which Gobuster scan type would you like? (vhost/dir): \n")
# Run Gobuster scan
if gobuster_type == "dir":
    gobuster_command = f"gobuster dir -u http://{ip_address} -w $DIRBIG -o {ip_address}_dir_gobuster.txt"
elif gobuster_type == "vhost":
    gobuster_command = f"gobuster vhost -u http://{ip_address} -w $DIRBIG -o {ip_address}_vhost_gobuster.txt"
else:
    print("Invalid scan type")
os.system(gobuster_command)


# Run dirb scan
dirb_command = f"dirb http://{ip_address} /usr/share/payloads/SecLists/Discovery/Web-Content/SVNDigger/all-dirs.txt -o {ip_address}_dirb.txt"
os.system(dirb_command)
# Print output file paths
print(f"Nmap output saved to {ip_address}_{scan_type}_nmap.txt")
if gobuster_type == "dir":
    print(f"Gobuster output saved to {ip_address}_dir_gobuster.txt")
if gobuster_type == "vhost":
    print(f"Gobuster output saved to {ip_address}_vhost_gobuster.txt")

print(f"dirb output saved to {ip_address}_dirb.txt")

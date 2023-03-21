import tkinkter as tk
from tkinter import ttk
import os
import subprocess
# Just a simple script to automate scan and enumeration 
# Made by: SparQz

# Create a Tkinter window and set its properties
root = tk.Tk()
root.title("Better Scan")
root.geometry("400x200")
root.resizable(False, False)

# Create a frame for the checkboxes
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Add the checkboxes

quick_scan_var = tk.BooleanVar()
quick_scan_cb = ttk.Checkbutton(frame, text="Quick Scan", variable=quick_scan_var)

full_scan_var = tk.BooleanVar()
full_scan_cb = ttk.Checkbutton(frame, text="Full Scan", variable=full_scan_var)
full_scan_cb.pack(anchor=tk.W)

dirb_frame= ttk.LabelFrame(root, text="Dirb")
dirb_frame.pack(padx=10, pady=10, fill=tk.X)

dirb_var= tk.BooleanVar()
dirb_cb= ttk.Checkbutton(dirb_frame, text="Enable Dirb", variable=dirb_var)
dirb_cb.pack(side=tk.LEFT)


gobuster_frame = ttk.LabelFrame(root, text="Gobuster")
gobuster_frame.pack(padx=10, pady=10, fill=tk.X)

gobuster_var= tk.BooleanVar()
gobuster_cb= ttk.Checkbutton(gobuster_frame, text="Enable Gobuster", variable=gobuster_var)
gobuster.pack(side=tk.LEFT)

dirb_options_frame = ttk.Frame(dirb_frame)
dirb_options_frame.pack(fill=tk.X)

gobuster_options_frame = ttk.Frame(gobuster_frame)
gobuster_options_frame.pack(fill=tk.X)

dirb_wordlist_var = tk.BooleanVar()
dirb_wordlist_cb = ttk.Checkbutton(dirb_options_frame, text="Use Wordlist", variable=dirb_wordlist_var)
dirb_wordlist_cb.pack(side=tk.LEFT)

gobuster_wordlist_var = tk.BooleanVar()
gobuster_wordlist_cb = ttk.Checkbutton(dirb_options_frame, text="Use Wordlist", variable=gobuster_wordlist_var)
gobuster_wordlist_cb.pack(side=tk.LEFT)


def run_scan():
    if quick_scan_var.get():
        # Run Quick scan
        nmap_command = f"nmap -sV -Pn {ip_address} -oN {ip_address}_nmap.txt"
    elif full_scan_var.get()
        # Run Full Scan
    else:
        echo "Incorrect scan type selected."
        
# Add a button to start the scan
scan_button =ttk.Button(root, text="Scan" , command=run_scan)
scan_button.pack(pady=10)

root.mainloop()


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

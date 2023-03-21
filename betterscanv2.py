import tkinter as tk
import subprocess

def scan():
	ip_address = ip_entry.get()
	options = ""
	if nmap_var.get():
		options +="-sS "
	if udp_scan_var.get():
		options += "-sU"
	if stealth_scan_var.get():
		options += "-sS -sV -T4 -O -F --version-light "
	if full_scan_var.get():
		options += "-sS -sV -sC -A -O -T4 "
	if os_fingerprint_var.get():
		options += "-O "
	if service_info_var.get():
		options += "-sV "
	subprocess.run(f"nmap {options} {ip_address}", shell=True)
	if gobuster_var.get():
		subprocess.run(f"gobuster dir -u http://{ip_address} -w /usr/share/payloads/SecLists/Discover/Web-Content/directory-list-2.3-medium.txt -x php, txt", shell=True)
		
	if dirb_var.get():
		subprocess.run(f"dirb http://{ip_address}", shell=True)

window = tk.Tk()
window.title("Over9000")

# IP address entry

ip_label = tk.Label(window, text="Enter IP Address: ")
ip_label.pack()
ip_entry = tk.Entry(window)
ip_entry.pack()


nmap_var = tk.BooleanVar()
nmap_check = tk.Checkbutton(window, text="nmap", variable=nmap_var)
nmap_check.pack()
udp_scan_var = tk.BooleanVar()
udp_scan_check = tk.Checkbutton(window, text="UDP Scan", variable=udp_scan_var)
udp_scan_check.pack()
stealth_scan_var = tk.BooleanVar()
stealth_scan_check = tk.Checkbutton(window, text="Stealth Scan", variable=stealth_scan_var)
stealth_scan_check.pack()
full_scan_var = tk.BooleanVar()
full_scan_check = tk.Checkbutton(window, text= "Full Scan", variable=full_scan_var)
full_scan_check.pack()
os_fingerprint_var = tk.BooleanVar()
os_fingerprint_check = tk.Checkbutton(window, text="OS Fingerprint", variable=os_fingerprint_var)
os_fingerprint_check.pack()
service_info_var = tk.BooleanVar()
service_info_check = tk.Checkbutton(window, text="Service Info", variable=service_info_var)
service_info_check.pack()
gobuster_var = tk.BooleanVar()
gobuster_check = tk.Checkbutton(window, text="gobuster", variable=gobuster_var)
gobuster_check.pack()
dirb_var = tk.BooleanVar()
dirb_check = tk.Checkbutton(window, text="dirb", variable=dirb_var)
dirb_check.pack()


# Scan Button
scan_button = tk.Button(window, text="Scan", command=scan)
scan_button.pack()

window.mainloop()


	


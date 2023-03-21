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
        
        elif full_scan_var.get()
        # Run Full Scan
    else:
        echo "Incorrect scan type selected."
        
# Add a button to start the scan
scan_button =ttk.Button(root, text="Scan" , command=run_scan)
scan_button.pack(pady=10)

root.mainloop()




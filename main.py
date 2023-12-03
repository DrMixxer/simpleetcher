import tkinter as tk
from tkinter import filedialog

def select_iso_location():
    iso_location = filedialog.askopenfilename(title="Select ISO Location")
    print("ISO Location:", iso_location)

def select_drive_location():
    drive_location = filedialog.askdirectory(title="Select Drive Location")
    print("Drive Location:", drive_location)

def perform_etching():
    print("Performing etching...")

root = tk.Tk()
root.geometry("256x256")

iso_button = tk.Button(root, text="ISO Location", command=select_iso_location)
iso_button.pack()

drive_button = tk.Button(root, text="Drive Location", command=select_drive_location)
drive_button.pack()

flash_button = tk.Button(root, text="Flash", command=perform_etching)
flash_button.pack()

root.mainloop()
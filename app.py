import tkinter as tk
from tkinter import filedialog
import os

def upload():
    file = filedialog.askopenfilename()
    label.config(text=file)

def print_file():
    if label.cget("text"):
        os.startfile(label.cget("text"), "print")

root = tk.Tk()
root.title("PVC Tool")

btn1 = tk.Button(root, text="Upload File", command=upload)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Print", command=print_file)
btn2.pack(pady=10)

label = tk.Label(root, text="No file selected")
label.pack()

root.mainloop()

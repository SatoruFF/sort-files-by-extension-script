import os
import tkinter as tk
from tkinter import filedialog

def sort_files(directory):
    files = os.listdir(directory)
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            extension = os.path.splitext(file)[1][1:]
            subdirectory = os.path.join(directory, extension)
            if not os.path.exists(subdirectory):
                os.makedirs(subdirectory)
            os.rename(os.path.join(directory, file), os.path.join(subdirectory, file))

def browse_folder():
    directory = filedialog.askdirectory(initialdir = "/", title = "Select a folder")
    sort_files(directory)
    result_label.config(text="Files sorted into subdirectories by extension.")

root = tk.Tk()
root.title("File Sorter")
root.geometry("300x100")

browse_button = tk.Button(text="Browse", command=browse_folder)
browse_button.pack(expand=True)

result_label = tk.Label(text="")
result_label.pack()

root.mainloop()

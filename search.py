import pandas as pd
import tkinter as tk
from tkinter import messagebox

def search_ip(entry, result_label):
    global var  # Make var a global variable
    df = pd.read_csv('sn.csv')
    search = entry.get()
    search_type = var.get()  # Get the selected search type

    print(df.columns)  # Print column names for debugging

    if search_type == "IP":
        result = df.loc[df['ip_addr'] == search]
    elif search_type == "SN":
        result = df.loc[df['serial_num'] == search]
    else:
        return

    result_label.config(text=str(result))

def main():
    global var  # Make var a global variable
    root = tk.Tk()
    root.title("IP Search App")

    label = tk.Label(root, text="Enter the search term:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    var = tk.StringVar(value="IP")  # Default search type is IP

    ip_button = tk.Radiobutton(root, text="IP", variable=var, value="IP")
    ip_button.pack()

    sn_button = tk.Radiobutton(root, text="SN", variable=var, value="SN")
    sn_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    button = tk.Button(root, text="Search", command=lambda: search_ip(entry, result_label))
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

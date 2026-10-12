import tkinter as tk
from tkinter import messagebox
import os

# این خط باعث می‌شود مسیرِ دقیقِ همین فایلِ پایتون پیدا شود
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "passwords.txt")

def save_password():
    website = website_entry.get()
    username = user_entry.get()
    password = pass_entry.get()

    if website == "" or password == "":
        messagebox.showwarning("error", "please enter your username, password, and website")
    else:
        # حالا از مسیرِ دقیق (FILE_PATH) استفاده می‌کنیم
        with open(FILE_PATH, "a", encoding="utf-8") as f:
            f.write(f"Web: {website} | User: {username} | Pass: {password}\n")
        
        website_entry.delete(0, 'end')
        user_entry.delete(0, 'end')
        pass_entry.delete(0, 'end')
        messagebox.showinfo("succes", "password saced succesfully")

root = tk.Tk()
root.title("Password Manager")
root.geometry("300x200")

tk.Label(root, text="Website:").grid(row=0, column=0, padx=10, pady=5)
website_entry = tk.Entry(root)
website_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Username:").grid(row=1, column=0, padx=10, pady=5)
user_entry = tk.Entry(root)
user_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=5)
pass_entry = tk.Entry(root, show="*")
pass_entry.grid(row=2, column=1, padx=10, pady=5)

save_btn = tk.Button(root, text="Save Password", command=save_password)
save_btn.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()

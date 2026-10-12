import tkinter as tk
from tkinter import messagebox
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "passwords.txt")

def save_password():
    website = website_entry.get()
    username = user_entry.get()
    password = pass_entry.get()

    if website == "" or password == "":
        messagebox.showwarning("خطا", "لطفاً وب‌سایت و پسورد را وارد کنید!")
    else:
        with open(FILE_PATH, "a", encoding="utf-8") as f:
            f.write(f"Web: {website} | User: {username} | Pass: {password}\n")
        
        website_entry.delete(0, 'end')
        user_entry.delete(0, 'end')
        pass_entry.delete(0, 'end')
        messagebox.showinfo("موفقیت", "پسورد ذخیره شد!")

def view_passwords():
    # باز کردن پنجره جدید
    if not os.path.exists(FILE_PATH):
        messagebox.showinfo("اطلاعات", "هنوز هیچ پسوردی ذخیره نشده است.")
        return
    
    view_win = tk.Toplevel(root)
    view_win.title("Saved Passwords")
    view_win.geometry("400x300")
    
    text_area = tk.Text(view_win, width=50, height=15)
    text_area.pack(pady=10)
    
    # خواندن فایل
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        text_area.insert("1.0", content)
    
    text_area.config(state="disabled") # غیرقابل ویرایش کردن برای امنیت

root = tk.Tk()
root.title("Password Manager")
root.geometry("300x250")

# UI Elements
tk.Label(root, text="Website:").grid(row=0, column=0, padx=10, pady=5)
website_entry = tk.Entry(root)
website_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Username:").grid(row=1, column=0, padx=10, pady=5)
user_entry = tk.Entry(root)
user_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=5)
pass_entry = tk.Entry(root, show="*")
pass_entry.grid(row=2, column=1, padx=10, pady=5)

# Buttons
save_btn = tk.Button(root, text="Save Password", command=save_password)
save_btn.grid(row=3, column=0, columnspan=2, pady=10)

view_btn = tk.Button(root, text="View All", command=view_passwords)
view_btn.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()

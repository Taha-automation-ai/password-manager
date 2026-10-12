import tkinter as tk
from tkinter import messagebox
import os
import random
import string
import base64  # کتابخانه استاندارد برای تبدیل به کدِ غیرخوانا

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "passwords.txt")

# توابع رمزنگاری و رمزگشایی
def encrypt(text):
    return base64.b64encode(text.encode()).decode()

def decrypt(text):
    return base64.b64decode(text.encode()).decode()

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(12))
    pass_entry.delete(0, 'end')
    pass_entry.insert(0, password)
    copy_to_clipboard(password)

def save_password():
    website = website_entry.get()
    username = user_entry.get()
    password = pass_entry.get()

    if website == "" or password == "":
        messagebox.showwarning("خطا", "لطفاً وب‌سایت و پسورد را وارد کنید!")
    else:
        # ذخیره با رمزنگاری
        encrypted_pass = encrypt(password)
        with open(FILE_PATH, "a", encoding="utf-8") as f:
            f.write(f"Web: {website} | User: {username} | Pass: {encrypted_pass}\n")
        
        copy_to_clipboard(password)
        website_entry.delete(0, 'end')
        user_entry.delete(0, 'end')
        pass_entry.delete(0, 'end')
        messagebox.showinfo("موفقیت", "پسورد امن ذخیره شد!")

def view_passwords():
    if not os.path.exists(FILE_PATH):
        messagebox.showinfo("اطلاعات", "هنوز هیچ پسوردی ذخیره نشده است.")
        return
    
    view_win = tk.Toplevel(root)
    view_win.title("Saved Passwords (Decrypted)")
    view_win.geometry("500x350")
    
    text_area = tk.Text(view_win, width=60, height=20)
    text_area.pack(pady=10)
    
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            # جدا کردن بخش پسورد و رمزگشایی آن
            if "| Pass: " in line:
                parts = line.split("| Pass: ")
                decrypted_pass = decrypt(parts[1].strip())
                text_area.insert("end", f"{parts[0]} | Pass: {decrypted_pass}\n")
    
    text_area.config(state="disabled")

root = tk.Tk()
root.title("Secure Password Manager")
root.geometry("300x350")

# UI Elements
tk.Label(root, text="Website:").grid(row=0, column=0, padx=10, pady=5)
website_entry = tk.Entry(root)
website_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Username:").grid(row=1, column=0, padx=10, pady=5)
user_entry = tk.Entry(root)
user_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=5)
pass_entry = tk.Entry(root)
pass_entry.grid(row=2, column=1, padx=10, pady=5)

gen_btn = tk.Button(root, text="Generate", command=generate_password)
gen_btn.grid(row=3, column=1, pady=5)

save_btn = tk.Button(root, text="Save Password", command=save_password)
save_btn.grid(row=4, column=0, columnspan=2, pady=10)

view_btn = tk.Button(root, text="View All", command=view_passwords)
view_btn.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()

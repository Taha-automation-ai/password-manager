import tkinter as tk
from tkinter import messagebox
import os
import random
import string # برای تولید حروف و اعداد تصادفی

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "passwords.txt")

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

# تابع جدید برای تولید پسورد
def generate_password():
    # ترکیب حروف بزرگ، کوچک، اعداد و کاراکترهای خاص
    chars = string.ascii_letters + string.digits + string.punctuation
    # ساخت پسورد 12 کاراکتری
    password = ''.join(random.choice(chars) for i in range(12))
    
    # نمایش در فیلد پسورد
    pass_entry.delete(0, 'end')
    pass_entry.insert(0, password)
    
    # کپی خودکار به کلیپ‌بورد برای راحتی بیشتر
    copy_to_clipboard(password)

def save_password():
    website = website_entry.get()
    username = user_entry.get()
    password = pass_entry.get()

    if website == "" or password == "":
        messagebox.showwarning("خطا", "لطفاً وب‌سایت و پسورد را وارد کنید!")
    else:
        with open(FILE_PATH, "a", encoding="utf-8") as f:
            f.write(f"Web: {website} | User: {username} | Pass: {password}\n")
        
        copy_to_clipboard(password)
        website_entry.delete(0, 'end')
        user_entry.delete(0, 'end')
        pass_entry.delete(0, 'end')
        messagebox.showinfo("موفقیت", "پسورد ذخیره و کپی شد!")

def view_passwords():
    if not os.path.exists(FILE_PATH):
        messagebox.showinfo("اطلاعات", "هنوز هیچ پسوردی ذخیره نشده است.")
        return
    
    view_win = tk.Toplevel(root)
    view_win.title("Saved Passwords")
    view_win.geometry("400x300")
    
    text_area = tk.Text(view_win, width=50, height=15)
    text_area.pack(pady=10)
    
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        text_area.insert("1.0", content)
    
    text_area.config(state="disabled")

root = tk.Tk()
root.title("Password Manager")
root.geometry("300x300") # پنجره را کمی بلندتر کردیم

tk.Label(root, text="Website:").grid(row=0, column=0, padx=10, pady=5)
website_entry = tk.Entry(root)
website_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Username:").grid(row=1, column=0, padx=10, pady=5)
user_entry = tk.Entry(root)
user_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=5)
pass_entry = tk.Entry(root, show="*")
pass_entry.grid(row=2, column=1, padx=10, pady=5)

# دکمه جدید برای تولید پسورد
gen_btn = tk.Button(root, text="Generate Password", command=generate_password)
gen_btn.grid(row=3, column=1, pady=5)

save_btn = tk.Button(root, text="Save Password", command=save_password)
save_btn.grid(row=4, column=0, columnspan=2, pady=10)

view_btn = tk.Button(root, text="View All", command=view_passwords)
view_btn.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()

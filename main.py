import tkinter as tk
from tkinter import *
from tkinter import ttk
import datauser as us
from tkinter import messagebox

user = us.DataUser("Dosen", "dosen123", "0", "admin")

class MainApp:

    def __init__(self,root):
        self.root = root
        self.root.title("Mbanking-Kelompok1")
        self.root.geometry("600x410")
        self.root.configure(bg="#2A1F3D")

        self.title = tk.Label(self.root, text="Hallo Kamu!!", font=("Segoe UI", 15, "bold"), bg="#ffffff")
        self.title.pack(pady=(20, 20))

        self.label = ttk.Label(root, text="Username",background="#83f9fd", font=("Comic Sans MS", 13, "bold"))
        self.label.pack()
        self.entry_username = ttk.Entry(self.root, width=30)
        self.entry_username.pack(pady=(0,10))

        self.label = ttk.Label(root, text="Passsword",background="#83d4fd", font=("Comic Sans MS", 13, "bold") )
        self.label.pack()
        self.entry_password = ttk.Entry(self.root,show="*", width=30)
        self.entry_password.pack(pady=(0,20))

        self.button = ttk.Button(self.root, text="Login",command=self.proses_login)

        self.button = tk.Button(self.root, text="Login", command=self.proses_login, font=("Segoe UI", 13, "bold"))
        self.button.pack(pady=15)

    def proses_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        print("Username:", username)
        print("Password:", password)
        datauser =  user.panggil_user(username,password)
        print(datauser)
        self.admin_login()

        if len(datauser):
            messagebox.showinfo("Success", f"Welcome {datauser[5]}!")
            self.admin_login()
            
        else :
            messagebox.showerror("Failed", "Invalid username or password")
             

    def admin_login(self):
        self.clear_window()
        tk.Label(self.root, text="MENU ADMIN BANK", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="Lihat Nasabah", width=25).pack(pady=5)
        tk.Button(self.root, text="Tambah Nasabah", width=25).pack(pady=5)
        tk.Button(self.root, text="Blokir Nasabah", width=25).pack(pady=5)
        tk.Button(self.root, text="Lihat Transaksi", width=25).pack(pady=5)
        tk.Button(self.root, text="Keluar", width=25, command=root.quit).pack(pady=20)


    def clear_window(self):
	    for widget in self.root.winfo_children():
	        widget.destroy()
root = Tk()
app = MainApp(root)
root.mainloop()


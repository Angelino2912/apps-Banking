import tkinter as tk
from tkinter import *
from tkinter import ttk
import datauser as us

user = us.DataUser("Dosen", "dosen123", "0", "admin")

class MainApp:

    def __init__(self,root):
        self.root = root
        self.root.title("Mbanking-Kelompok1")
        self.root.geometry("600x410")
        self.root.configure(bg="#2A1F3D")

        self.title = tk.Label(self.root, text="Hallo Kamu!!", font=("Segoe UI", 15, "bold"), bg="#ffffff")
        self.title.pack(pady=(20, 20))

        self.label = ttk.Label(root, text="Username",background="#fd83f1", font=("Comic Sans MS", 13, "bold"))
        self.label.pack()
        self.entry_username = ttk.Entry(self.root, width=30)
        self.entry_username.pack(pady=(0,10))

        self.label = ttk.Label(root, text="Passsword",background="#fd83f1", font=("Comic Sans MS", 13, "bold") )
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

        if len(datauser):
            print("login berhasil")
            print(f"anda login sebagai {datauser[5]}")
             
        else:
            print("Username or Password salah")


root = Tk()
app = MainApp(root)
root.mainloop()


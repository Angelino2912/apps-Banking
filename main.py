import tkinter as tk
from tkinter import *
from tkinter import ttk
import datauser as us
from tkinter import messagebox


user = us.DataUser("Dosen", "dosen123", "0", "admin")
user_repo = us.UserRepository()


class MainApp:

    def __init__(self,root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("600x410")
        self.root.configure(bg="#2A1F3D")

        self.title = tk.Label(self.root, text="Hallo Kamu!!", font=("Segoe UI", 15, "bold"), bg="#ffffff")
        self.title.pack(pady=(20, 20))

        self.label = ttk.Label(root, text="Username",background="#83f9fd", font=("Comic Sans MS", 13, "bold"))
        self.label.pack()
        self.entry_username = ttk.Entry(self.root, width=30)
        self.entry_username.pack(pady=(0,10))

        self.label = ttk.Label(root, text="Passsword",background="#83f9fd", font=("Comic Sans MS", 13, "bold") )
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
        datauser = user_repo.panggil_user(username, password)
        print(datauser)
       
        if datauser is not None:
            nama = datauser[2]   

            messagebox.showinfo("Success", f"Welcome {datauser[5]}!")
            self.admin_login()  

        else:
            messagebox.showerror("Failed", "Invalid username or password")

    def admin_login(self):
        self.clear_window()

        self.root.title("admin login")
        self.root.geometry("600x410")
        self.root.configure(bg="#2A1F3D")
        
        tk.Label(self.root, text="MENU ADMIN BANK", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="Lihat Nasabah", width=25, command=self.lihat_nasabah).pack(pady=5)
        tk.Button(self.root, text="Tambah Nasabah", width=25, command=self.tambah_nasabah).pack(pady=5)
        tk.Button(self.root, text="Blokir Nasabah", width=25).pack(pady=5)
        tk.Button(self.root, text="Lihat Transaksi", width=25).pack(pady=5)
        tk.Button(self.root, text="Keluar", width=25, command=root.quit).pack(pady=20)

        
    def lihat_nasabah(self):
        self.clear_window()
        self.root.title("Nasabah Page")
        self.root.geometry("600x410")
        self.root.configure(bg="#2A1F3D")

        datauser = user_repo.ambil_user()
        print(datauser)

        data_customer = [row for row in datauser if row.role_us == "customer"]


        columns = ("username_us", "password_us", "balance", "role_us")
        tree = ttk.Treeview(self.root, columns=columns, show="headings")
        tree.pack(fill="both", expand=True, padx=20, pady=20)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor="center")

        
        for row in data_customer:
            tree.insert("", "end", values=row.as_tuple())

    def tambah_nasabah(self):
        self.clear_window()
        self.root.title("Tambah Nasabah")
        self.root.geometry("400x350")
        self.root.configure(bg="#2A1F3D")

        tk.Label(self.root, text="Tambah Nasabah Baru", font=("Arial", 16), bg="#2A1F3D", fg="white").pack(pady=20)

        frame = tk.Frame(self.root, bg="#2A1F3D")
        frame.pack()

        tk.Label(frame, text="Username:", bg="#2A1F3D", fg="white").grid(row=0, column=0, pady=5)
        entry_user = tk.Entry(frame, width=30)
        entry_user.grid(row=0, column=1)

        tk.Label(frame, text="Password:", bg="#2A1F3D", fg="white").grid(row=1, column=0, pady=5)
        entry_pass = tk.Entry(frame, width=30, show="*")
        entry_pass.grid(row=1, column=1)

        tk.Label(frame, text="Saldo Awal:", bg="#2A1F3D", fg="white").grid(row=2, column=0, pady=5)
        entry_saldo = tk.Entry(frame, width=30)
        entry_saldo.grid(row=2, column=1)

        def proses_tambah():
            username = entry_user.get()
            password = entry_pass.get()
            saldo = entry_saldo.get()

            if username == "" or password == "" or saldo == "":
                messagebox.showerror("Error", "Semua field wajib diisi!")
                return
            
            new_user = us.DataUser(username, password, saldo, "customer")
            user_repo.tambah_user(new_user)

            messagebox.showinfo("Sukses", "Nasabah berhasil ditambahkan!")
            self.admin_login()

        tk.Button(self.root, text="Simpan", command=proses_tambah).pack(pady=20)


        
       
         
         



    
    
    def clear_window(self):
	    for widget in self.root.winfo_children():
	        widget.destroy()

    # def clear_content(self):
	#     if hasattr(self, "content_frame") and self.content_frame.winfo_exists():
	#         for widget in self.content_frame.winfo_children():
	#             widget.destroy()

root = Tk()
app = MainApp(root)
root.mainloop()


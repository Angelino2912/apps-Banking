import tkinter as tk
from tkinter import *
from tkinter import ttk
import datauser as us
from tkinter import messagebox
from datauser import UserRepo

# pemilaian presentasi, penilaian laporan, nilai aplikasi, nilai konntribusi, nilai tanya jawab.


user = us.DataUser("Dosen", "dosen123", "0", "admin")
user_repo = us.UserRepo()


class MainApp:

    def __init__(self,root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("600x410")


        self.root.configure(bg="#2A1F3D")
        self.login_page()

        self.root.configure(bg="#FFFFFF")


        self.root.configure(bg="#2A1F3D")
        self.login_page()


    def login_page(self):

        self.clear_window()
        # menghilangkan tampilan sebelumnya sebelum keluar pagenya
 
        self.title = tk.Label(self.root, text="Hallo Kamu!!", font=("Segoe UI", 15, "bold"), bg="#ffffff")
        self.title.pack(pady=(20, 20))

        self.label = ttk.Label(root, text="Username",background="#ffffff", font=("Comic Sans MS", 13, "bold"))
        self.label.pack()
        self.entry_username = ttk.Entry(self.root, width=30)
        self.entry_username.pack(pady=(0,10))

        self.label = ttk.Label(root, text="Passsword",background="#83f9fd", font=("Comic Sans MS", 13, "bold") )

        self.label = ttk.Label(root, text="Passsword",background="#ffffff", font=("Comic Sans MS", 13, "bold") )


        self.label.pack()
        self.entry_password = ttk.Entry(self.root,show="*", width=30)
        self.entry_password.pack(pady=(0,20))

        self.button = ttk.Button(self.root, text="Login",command=self.proses_login)

        self.button = tk.Button(self.root, text="Login", command=self.proses_login, font=("Segoe UI", 13, "bold"))
        self.button.pack(pady=15)

    def proses_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.current_user = user_repo.panggil_user(username, password)

        if not self.current_user:
            messagebox.showerror("Failed", "Invalid username or password")
            return

        if self.current_user.role_us == "customer":
            messagebox.showinfo("Success", f"Welcome {self.current_user.username_us}!")
            self.cust_login()
        elif self.current_user.role_us == "admin":
            messagebox.showinfo("Success", f"Welcome {self.current_user.username_us}!")
            self.admin_login()
    
    def admin_login(self):
        self.clear_window()

        self.root.title("admin login")
        self.root.geometry("600x410")
        self.root.configure(bg="#2A1F3D")

   
        tk.Label(self.root, text="MENU ADMIN BANK", font=("Arial", 16), bg="#2A1F3D", fg="white").pack(pady=20)
        tk.Button(self.root, text="Lihat Nasabah", width=25, command=self.lihat_nasabah).pack(pady=5)
        tk.Button(self.root, text="Tambah Nasabah", width=25, command=self.tambah_nasabah).pack(pady=5)
        tk.Button(self.root, text="Lihat Transaksi", width=25).pack(pady=5)
        tk.Button(self.root, text="Keluar", width=25, command=self.login_page).pack(pady=20)
   
    def lihat_nasabah(self):
        self.clear_window()
        data_customer = user_repo.ambil_user()

        columns = ("No Rek", "Username", "Password", "Saldo", "Role")

        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.tree.pack(fill="both", expand=True, padx=20, pady=20)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")

        for row in data_customer:
            self.tree.insert("", "end", values=(
                row.no_rek,
                row.username_us,
                row.password_us,
                row.balance,
                row.role_us
            ))

            self.load_data

        tk.Button(self.root, text="Kembali", command=self.admin_login).pack(pady=10)

    def load_data(self):
        repo = UserRepo()
        data = repo.ambil_semua_user()  

        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in data:
            self.tree.insert("", "end", values=row)

    def tambah_nasabah(self):
        self.clear_window()
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
            
            if not username or not password or not saldo:
                messagebox.showerror("Error", "Semua field wajib diisi!")
                return
            
            new_user = us.DataUser(username, password, int(saldo), "customer")
            user_repo.tambah_user(new_user)
            messagebox.showinfo("Sukses", "Nasabah berhasil ditambahkan!")
            self.admin_login()

        tk.Button(self.root, text="Simpan", command=proses_tambah).pack(pady=10)
        tk.Button(self.root, text="Kembali", command=self.admin_login).pack(pady=5)
    

    def cust_login(self):
        self.clear_window()
        self.root.title("Customer Menu")

        tk.Label(self.root,
                 text=f"Selamat datang, {self.current_user.username_us}",
                 font=("Arial", 14), bg="#2A1F3D", fg="white").pack(pady=15)

        tk.Button(self.root, text="Cek Saldo", width=20, command=self.cek_saldo).pack(pady=5)
        tk.Button(self.root, text="Setor / Deposit", width=20, command=self.menu_deposit).pack(pady=5)
        tk.Button(self.root, text="Tarik Tunai", width=20, command=self.menu_withdraw).pack(pady=5)
        tk.Button(self.root, text="Riwayat Transaksi", width=20, command=self.menu_history).pack(pady=5)
        tk.Button(self.root, text="Logout", width=10, command=self.login_page).pack(pady=20)
 
    def cek_saldo(self):
        saldo = int(self.current_user.balance)
        formatted_saldo = f"Rp {saldo:,.0f}"
        
        top = tk.Toplevel(self.root)
        top.title("Saldo Anda")
        top.geometry("500x500")
        top.configure(bg="#2A1F3D")
        
        tk.Label(top, text=f"👋 Halo Cust {self.current_user.username_us}!", 
                font=("Arial", 14), bg="#2A1F3D", fg="white").pack(pady=10)
        
        tk.Label(top, text=f"💰 Saldo Anda Saat ini: {formatted_saldo}", 
                font=("Arial", 16, "bold"), bg="#2A1F3D", fg="white").pack(pady=10)
        
        tk.Button(top, text="Tutup", command=top.destroy).pack(pady=10)
   
    def menu_deposit(self):
        self.clear_window()
        
        tk.Label(self.root, text="Setor / Deposit", font=("Arial", 14), bg="#2A1F3D", fg="white").pack(pady=20)
        tk.Label(self.root, text="Masukkan nominal:", bg="#2A1F3D", fg="white").pack()
        
        amount = tk.Entry(self.root)
        amount.pack(pady=5)

        def proses():
            try:
                nominal = int(amount.get())
                if nominal <= 0:
                    raise ValueError
                
                self.current_user.balance += nominal
                self.current_user.add_history(f"Deposit: +Rp {nominal}")
                
                user_repo.save_history(
                self.current_user.username_us,"Deposit",+nominal
                )
                
                user_repo.update_balance(self.current_user)

                messagebox.showinfo("Sukses", "Deposit berhasil!")
                self.cust_login()
            except:
                messagebox.showerror("Error", "Nominal tidak valid!")

        tk.Button(self.root, text="Setor", command=proses).pack(pady=10)
        tk.Button(self.root, text="Kembali", command=self.cust_login).pack(pady=5)

    def menu_withdraw(self):
        self.clear_window()
        
        tk.Label(self.root, text="Tarik Tunai", font=("Arial", 14), bg="#2A1F3D", fg="white").pack(pady=20)
        tk.Label(self.root, text="Masukkan nominal:", bg="#2A1F3D", fg="white").pack()
        
        amount = tk.Entry(self.root)
        amount.pack(pady=5)

        def proses():
            try:
                nominal = int(amount.get())
                if nominal <= 0 or nominal > self.current_user.balance:
                    raise ValueError
                self.current_user.balance -= nominal
                self.current_user.add_history(f"Withdraw: -Rp {nominal}")
                
                user_repo.save_history(
                self.current_user.username_us,"Withdraw",-nominal
                )
               
                user_repo.update_balance(self.current_user)   

                messagebox.showinfo("Sukses", "Penarikan berhasil!")
                self.cust_login()
            except:
                messagebox.showerror("Error", "Nominal tidak valid atau saldo kurang!")
        
        tk.Button(self.root, text="Tarik", command=proses).pack(pady=10)
        tk.Button(self.root, text="Kembali", command=self.cust_login).pack(pady=5)

    def menu_history(self):
        self.clear_window()
        
        tk.Label(self.root, text="Riwayat Transaksi", font=("Arial", 14), bg="#2A1F3D", fg="white").pack(pady=10)
        
        history_box = tk.Listbox(self.root, width=60, height=12)
        history_box.pack(pady=10)

        
        history_data = user_repo.get_history(self.current_user.username_us)
        
        if history_data:
            for desc, amount, time in history_data:
                history_box.insert(tk.END, f"{time} | {desc} | Rp {amount}")
        else:
            history_box.insert(tk.END, "Belum ada transaksi.")
        
        tk.Button(self.root, text="Kembali", command=self.cust_login).pack(pady=10)


       
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


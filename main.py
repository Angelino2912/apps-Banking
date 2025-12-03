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
        self.root.state("zoomed")  # buka window fullscreen
        self.login_page()


    def login_page(self):
        self.clear_window()

        # warna = hijau + background soft
        top_color = "#0BA68B"
        background= "#F5FAFC"

        # header hijau di atas
        self.top_frame = tk.Frame(self.root, bg=top_color, height=80)
        self.top_frame.pack(side="top", fill="x")
        self.top_frame.pack_propagate(False)
        ttk.Label(self.top_frame, text="Bank Kita Bersama",background=top_color, foreground="white",font=("Segoe UI", 25, "bold")).pack(pady=18)

        # area utama
        self.main_frame = tk.Frame(self.root, bg= background)
        self.main_frame.pack(fill="both", expand=True)

        # kartu form sederhana di tengah
        self.card = ttk.Frame(self.main_frame, padding=28)
        self.card.place(relx=0.5, rely=.4, anchor="center")

        ttk.Label(self.card, text="Silahkan Login", font=("Segoe UI", 15, "bold")).pack(pady=(0,9))

        ttk.Label(self.card, text="Username", font =("Arial", 9, "bold")).pack(anchor="w")
        self.entry_username = ttk.Entry(self.card, width=44)
        self.entry_username.pack(pady=6)

        ttk.Label(self.card, text="Password", font =("Arial", 9, "bold")).pack(anchor="w")
        self.entry_password = ttk.Entry(self.card, width=44, show="*")
        self.entry_password.pack(pady=6)

        # tombol tk supaya warna konsisten
        self.button = tk.Button(self.card, text="Login", command=self.proses_login,bg=top_color, fg="white", bd=0, width=28)
        self.button.pack(pady=(10,0))

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

        top_color = "#0BA68B"
        bg_main = "#F5FAFC"

        # header hijau
        self.top_frame = tk.Frame(self.root, bg=top_color, height=72)
        self.top_frame.pack(side="top", fill="x")
        self.top_frame.pack_propagate(False)
        ttk.Label(self.top_frame, text="Bank Kita Bersama — Admin", background=top_color,
                  foreground="white", font=("Segoe UI", 18, "bold")).pack(pady=16)

        # area utama
        self.main_frame = tk.Frame(self.root, bg=bg_main)
        self.main_frame.pack(fill="both", expand=True)

        # kartu sederhana di tengah
        self.card = ttk.Frame(self.main_frame, padding=(20,16))
        self.card.place(relx=0.5, rely=0.35, anchor="center")

        ttk.Label(self.card, text="MENU ADMIN", font=("Segoe UI", 14, "bold")).pack(pady=(0,12))

        # tombol berwarna (pakai tk.Button agar warna konsisten)
        tk.Button(self.card, text="Lihat Nasabah", width=28, command=self.lihat_nasabah,bg=top_color, fg="white", bd=0).pack(pady=6)
        tk.Button(self.card, text="Tambah Nasabah", width=28, command=self.tambah_nasabah,bg=top_color, fg="white", bd=0).pack(pady=6)
        tk.Button(self.card, text="Lihat Transaksi", width=28,bg=top_color, fg="white", bd=0).pack(pady=6)
        tk.Button(self.card, text="Ganti Password Nasabah", width=28,command=self.ganti_password,bg=top_color, fg="white", bd=0).pack(pady=6)

        # tombol kembali / logout
        tk.Button(self.card, text="Keluar", width=20, command=self.login_page,bg="#E53E3E", fg="white", bd=0).pack(pady=(12,0))

    def lihat_nasabah(self):
        self.clear_window()

        top_color = "#0BA68B"
        bg_main = "#F5FAFC"

        # self.root.title("Daftar Nasabah")
        # self.root.configure(bg=bg_main)

        # header hijau
        self.top_frame = tk.Frame(self.root, bg=top_color, height=72)
        self.top_frame.pack(side="top", fill="x")
        self.top_frame.pack_propagate(False) #untuk mengatur secara otomatis ukuran frame
        ttk.Label(self.top_frame, text="Daftar Nasabah", background=top_color,foreground="white", font=("Segoe UI", 18, "bold")).pack(pady=16)

        # area utama
        self.main_frame = tk.Frame(self.root, bg=bg_main)
        self.main_frame.pack(fill="both", expand=True) # untuk mengisi frame secara penuh jika "true",mengambil tinggi dan lebar

        # kartu berisi tabel
        self.card = ttk.Frame(self.main_frame, padding=(12,12))
        self.card.place(relx=0.5, rely=0.45, anchor="center") #relx=horizontal, rely=vertical 

        # style treeview nampilkan data
        style = ttk.Style()
        style.configure("Treeview", rowheight=28, font=("Segoe UI", 10))
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))

        # kolom (id internal -> label)
        cols = [("no_rek", "No Rek", 140, "center"),
                ("username_us", "Username", 220, "w"),
                ("password_us", "Password", 180, "center"),
                ("balance", "Saldo", 160, "center"),
                ("role_us", "Role", 120, "center")]

        table_frame = ttk.Frame(self.card)
        table_frame.pack(fill="both", expand=True)

        vsb = ttk.Scrollbar(table_frame, orient="vertical") #vertical scrollbar
        hsb = ttk.Scrollbar(table_frame, orient="horizontal")#horizontal scroll bar
        self.tree = ttk.Treeview(table_frame,
                                 columns=[c[0] for c in cols],
                                 show="headings",
                                 yscrollcommand=vsb.set, # menghubungkan dengan scrollbar
                                 xscrollcommand=hsb.set,
                                 height=12)
        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)

        #grid= lebih simple dari pack()
        self.tree.grid(row=0, column=0, sticky="nsew") #memenuhi seluruh area
        vsb.grid(row=0, column=1, sticky="ns")# vertikal
        hsb.grid(row=1, column=0, sticky="ew")# horizontal
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        # setup heading & column properties
        for col_id, label, width, anchor in cols:
            self.tree.heading(col_id, text=label)
            self.tree.column(col_id, width=width, anchor=anchor, stretch=True)

        # alternating row colors
        self.tree.tag_configure("odd", background="#FFFFFF")
        self.tree.tag_configure("even", background="#F3FFF9")

        # isi data dan format saldo
        data_customer = user_repo.ambil_user()
        for i, row in enumerate(data_customer):
            if data_customer:
                saldo_val = int(row.balance)
                saldo_text = f"Rp {saldo_val:,.0f}" # angka tertentu
            else:
                saldo_text = str(row.balance)

            values = (
                row.no_rek,
                row.username_us,
                row.password_us,
                saldo_text,
                row.role_us
            )
            tag = "even" if i % 2 == 0 else "odd" #jika genap dan ganjil
            self.tree.insert("", "end", values=values, tags=(tag,)) #menambahkan, tidak ada root lansung, baris akhir

        # tombol kembali di bawah
        button_frame = ttk.Frame(self.main_frame)
        button_frame.place(relx=0.5, rely=0.88, anchor="center") #relx=horizontal rely=vertical
        tk.Button(button_frame, text="Kembali", width=20, command=self.admin_login,bg=top_color, fg="white", bd=0).pack() #foreground

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


    def ganti_password(self):
        self.clear_window()
        self.root.title("Ganti Password Nasabah")
        self.root.configure(bg="#2A1F3D")

        tk.Label(self.root, text="Change Password Here BROOO !!!",font=("Arial", 16, "bold"), bg="#2A1F3D", fg="white").pack(pady=15)
        tk.Label(self.root, text="Username Customer", font=("Arial", 12), bg="#2A1F3D", fg="white").pack(pady=(10, 0))

        self.entry_username = tk.Entry(self.root, width=30)
        self.entry_username.pack(pady=5)

        tk.Label(self.root, text="Password Lama", font=("Arial", 12), bg="#2A1F3D", fg="white").pack(pady=(10, 0))

        self.entry_pass_lama = tk.Entry(self.root, width=30, show="*")
        self.entry_pass_lama.pack(pady=5)

        tk.Label(self.root, text="Password Baru", font=("Arial", 12), bg="#2A1F3D", fg="white").pack(pady=(10, 0))

        self.entry_pass_baru = tk.Entry(self.root, width=30, show="*")
        self.entry_pass_baru.pack(pady=5)

        tk.Label(self.root, text="Confirm Password baru", font=("Arial", 12), bg="#2A1F3D", fg="white").pack(pady=(10, 0))

        self.entry_confirm_pass = tk.Entry(self.root, width=30, show="*")
        self.entry_confirm_pass.pack(pady=5)

        tk.Button(self.root, text="Ganti Password", font=("Arial", 12, "bold"),bg="#4CAF50", fg="white",width=20,
                command=self.proses_ganti).pack(pady=20)
        
        tk.Button(self.root, text="kembali", font=("Arial", 12, "bold"),bg="#4CAF50", fg="white",width=20,command=self.admin_login).pack(pady=20)
    def proses_ganti(self):
        username = self.entry_username.get()
        password_lama = self.entry_pass_lama.get()
        password_baru = self.entry_pass_baru.get()
        confirm_pass = self.entry_confirm_pass.get()

        if not username or not password_lama or not password_baru:
            # Jika username,password lama, password baru salah satu ada yang kosong maka akan true
            # Jika true maka akan eror 
            # ini untuk mencegah user mencoba ganti password baru tanpa mengisi password lama dan username
            #  atau sebaliknya
            messagebox.showerror("Error", "Semua field harus diisi!")
            return
        # return:
        # Hentikan fungsi ini segera
        # Jangan lanjut ke proses berikutnya
        # Tidak melakukan pengecekan password lama
        # Tidak meng-update password
        # Tidak menyentuh database

        if password_baru != confirm_pass:
            # jika pass baru tidak sama dengan confirm pass maka akan eror
            messagebox.showerror("Error", "Konfirmasi password tidak sama!")
            return

        userRepo = UserRepo()
        success = userRepo.update_password(username, password_lama, password_baru)
        # jika username dan pass lama benar = berhasil
        # untuk menjalankan update password


        if success:
            # Berhasil → success = True
            # Gagal → success = False
            messagebox.showinfo("Success", "Password berhasil diganti!")
            self.entry_pass_lama.delete(0, tk.END)
            self.entry_pass_baru.delete(0, tk.END)
            self.entry_confirm_pass.delete(0, tk.END)
            # delete(0, tk.END) berarti:
            # hapus dari karakter index 0 sampai akhir (tk.END)
            # tujuanya agar password lama dan baru yang sudah diketik akan langsung hilang agar aman
        else:
            messagebox.showerror("Error", "Password lama salah atau user tidak ditemukan!")
        
     


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
        
        tk.Label(top, text=f" Halo Cust {self.current_user.username_us}!", 
                font=("Arial", 14), bg="#2A1F3D", fg="white").pack(pady=10)
        
        tk.Label(top, text=f" Saldo Anda Saat ini: {formatted_saldo}", 
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


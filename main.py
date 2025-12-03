import tkinter as tk
from tkinter import *
from tkinter import ttk
import datauser as us
from tkinter import messagebox
from datauser import UserRepo
from datetime import datetime

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
        ttk.Label(self.top_frame, text="Bank Kita Bersama — Admin", background=top_color,foreground="white", font=("Segoe UI", 18, "bold")).pack(pady=16)

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

        # header hijau
        self.top_frame = tk.Frame(self.root, bg=top_color, height=72)
        self.top_frame.pack(side="top", fill="x")
        self.top_frame.pack_propagate(False)
        ttk.Label(self.top_frame, text="Daftar Nasabah", background=top_color,foreground="white", font=("Segoe UI", 18, "bold")).pack(pady=16)
        #foreground=warna tulisan

        # area utama
        self.main_frame = tk.Frame(self.root, bg=bg_main)
        self.main_frame.pack(fill="both", expand=True)

        # kartu berisi tabel
        self.card = ttk.Frame(self.main_frame, padding=12)
        self.card.pack(fill="both", expand=True, padx=20, pady=20)

        # style treeview
        style = ttk.Style()
        style.configure("Treeview", rowheight=28, font=("Segoe UI", 10))
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))

        # treeview sederhana
        cols = ["No Rek", "Username", "Password", "Saldo", "Role"]
        self.tree = ttk.Treeview(self.card, columns=cols, show="headings", height=12)
        self.tree.pack(fill="both", expand=True)

        # setup heading & column
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=140, anchor="center")

        # alternating row colors
        self.tree.tag_configure("odd", background="#FFFFFF")
        self.tree.tag_configure("even", background="#F3FFF9")

        # isi data
        data_customer = user_repo.ambil_user()
        for i, row in enumerate(data_customer): #mengambil data dari databse sesuai list
            saldo_text = f"Rp {int(row.balance):,.0f}" #format saldo dengan koma pada nominal
            values = (row.no_rek, row.username_us, row.password_us, saldo_text, row.role_us) #menyusun data yang di tampilkan
            tag = "even" if i % 2 == 0 else "odd" #menentukan ganjil genap untuk pewarnaan nya biar cantik aja
            self.tree.insert("", "end", values=values, tags=(tag,))

        # tombol kembali
        tk.Button(self.root, text="Kembali", command=self.admin_login,bg=top_color, fg="white", bd=0, width=20).pack(pady=10)

    def load_data(self):
        repo = UserRepo()
        data = repo.ambil_semua_user()  

        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in data:
            self.tree.insert("", "end", values=row)

    def tambah_nasabah(self):
        self.clear_window()

        top_color = "#0BA68B"
        bg_main = "#F5FAFC"

        # header hijau
        self.top_frame = tk.Frame(self.root, bg=top_color, height=72)
        self.top_frame.pack(side="top", fill="x")
        self.top_frame.pack_propagate(False)#mengatur ukuran frame
        ttk.Label(self.top_frame, text="Tambah Nasabah", background=top_color,foreground="white", font=("Segoe UI", 18, "bold")).pack(pady=16)
        #foreground=warna tulisan

        # area utama
        self.main_frame = tk.Frame(self.root, bg=bg_main)
        self.main_frame.pack(fill="both", expand=True)

        # kartu sederhana di tengah
        self.card = ttk.Frame(self.main_frame, padding=20)
        self.card.place(relx=0.5, rely=0.35, anchor="center")

        ttk.Label(self.card, text="Form Tambah Nasabah", font=("Segoe UI", 14, "bold")).pack(pady=(0,12))

        ttk.Label(self.card, text="Username").pack(anchor="w")
        entry_user = ttk.Entry(self.card, width=44)
        entry_user.pack(pady=6)

        ttk.Label(self.card, text="Password").pack(anchor="w")
        entry_pass = ttk.Entry(self.card, width=44, show="*")
        entry_pass.pack(pady=6)

        ttk.Label(self.card, text="Saldo Awal").pack(anchor="w")
        entry_saldo = ttk.Entry(self.card, width=44)
        entry_saldo.pack(pady=6)

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

        tk.Button(self.card, text="Simpan", command=proses_tambah,bg=top_color, fg="white", bd=0, width=20).pack(pady=(10,6))
        tk.Button(self.card, text="Kembali", command=self.admin_login,bg="#E53E3E", fg="white", bd=0, width=20).pack()

    def ganti_password(self):
        self.clear_window()

        top_color = "#0BA68B"
        bg_main = "#F5FAFC"

        # header hijau
        self.top_frame = tk.Frame(self.root, bg=top_color, height=72)
        self.top_frame.pack(side="top", fill="x")
        self.top_frame.pack_propagate(False)#mengatur ukuran frame
        ttk.Label(self.top_frame, text="Ganti Password Nasabah", background=top_color,foreground="white", font=("Segoe UI", 18, "bold")).pack(pady=16)

        # area utama
        self.main_frame = tk.Frame(self.root, bg=bg_main) 
        self.main_frame.pack(fill="both", expand=True) #mengisi frame secara penuh

        # kartu sederhana di tengah
        self.card = ttk.Frame(self.main_frame, padding=20)
        self.card.place(relx=0.5, rely=0.35, anchor="center") #relx=horizontal, rely=vertical

        ttk.Label(self.card, text="Pergantian Password", font=("Segoe UI", 14, "bold")).pack(pady=(0,12))

        ttk.Label(self.card, text="Username Customer").pack(anchor="w")
        self.entry_username = ttk.Entry(self.card, width=44)
        self.entry_username.pack(pady=6)

        ttk.Label(self.card, text="Password Lama").pack(anchor="w")
        self.entry_pass_lama = ttk.Entry(self.card, width=44, show="*")
        self.entry_pass_lama.pack(pady=6)

        ttk.Label(self.card, text="Password Baru").pack(anchor="w")
        self.entry_pass_baru = ttk.Entry(self.card, width=44, show="*")
        self.entry_pass_baru.pack(pady=6)

        ttk.Label(self.card, text="Konfirmasi Password Baru").pack(anchor="w")
        self.entry_confirm_pass = ttk.Entry(self.card, width=44, show="*")
        self.entry_confirm_pass.pack(pady=6)

        tk.Button(self.card, text="Ganti Password", command=self.proses_ganti,bg=top_color, fg="white", bd=0, width=20).pack(pady=(10,6))
        tk.Button(self.card, text="Kembali", command=self.admin_login,bg="#E53E3E", fg="white", bd=0, width=20).pack()

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
           
    
            for desc, amount, timestamp in history_data:
                tampil = datetime.strptime(str(timestamp), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y %H:%M:%S")
                history_box.insert(tk.END, f"{tampil} | {desc} | Rp {amount}")
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


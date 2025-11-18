from tkinter import *
from tkinter import ttk
import datauser as us


user = us.datauser("Test 1","123456789","0")

class MainApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Mbanking-Angelino")
        self.root.geometry("480x210")

        self.label = ttk.Label(root, text="Username")
        self.label.pack()
        self.entry_username = ttk.Entry(self.root)
        self.entry_username.pack()

        
        self.label = ttk.Label(root, text="Passsword")
        self.label.pack()
        self.entry_password = ttk.Entry(self.root,show="*")
        self.entry_password.pack()

        self.button = ttk.Button(self.root, text="Login",command=self.proses_login)

        self.button = ttk.Button(self.root, text="Login", command=self.proses_login)
        self.button.pack(pady=10)

    def proses_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        print("Username:", username)
        print("Password:", password)
        user_login =  user.panggil_user(username,password)
        print(user_login)

        if len(user_login):
            print("login berhasil")
            print(f"anda login sebagai {user_login[2]}")
             
        else:
            print("Username or Password salah")

root = Tk()
app = MainApp(root)
root.mainloop()


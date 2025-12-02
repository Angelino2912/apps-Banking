
import database
import random
from datetime import datetime

def generate_rekening():
    return str(random.randint(100000, 999999))

class DataUser:
    def __init__(self, username_us, password_us, balance, role_us):
        self.no_rek = generate_rekening()
        self.username_us = username_us
        self.password_us = password_us
        self.balance = int(balance)
        self.role_us = role_us
        self.history = []
        
    def add_history(self, msg):
        self.history.append(msg)

    def insert_user(self):
        query = """
            INSERT INTO datauser (no_rek, username_us, password_us, balance, role_us)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (self.no_rek, self.username_us, self.password_us, self.balance, self.role_us)
        database.db.cursor.execute(query, values)
        database.db.mydb.commit()
        print("User berhasil ditambahkan! Rek:", self.no_rek)

class UserRepo:
    def __init__(self):
        self.db = database.db

    def ambil_user(self):
        sql = "SELECT username_us, password_us, balance, role_us FROM datauser WHERE role_us = 'customer'"
        self.db.cursor.execute(sql)
        results = self.db.cursor.fetchall()
        users = [DataUser(r[0], r[1], r[2], r[3]) for r in results]
        return users

    def panggil_user(self, username, password):
        sql = "SELECT username_us, password_us, balance, role_us FROM datauser WHERE username_us = %s AND password_us = %s"
        values = (username, password)
        self.db.cursor.execute(sql, values)
        row = self.db.cursor.fetchone()
        if row:
            return DataUser(row[0], row[1], row[2], row[3])
        return None
    
    def ambil_semua_user(self):
        sql = "SELECT no_rek, username_us, balance, role_us FROM datauser"
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()

    def tambah_user(self, user: DataUser):
        query = """
            INSERT INTO datauser (no_rek, username_us, password_us, balance, role_us)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (user.no_rek, user.username_us, user.password_us, user.balance, user.role_us)
        self.db.cursor.execute(query, values)
        self.db.mydb.commit()
        print("User berhasil ditambahkan melalui UserRepository! Rek:", user.no_rek)
      

    def update_balance(self, user: DataUser):
        sql = "UPDATE datauser SET balance = %s WHERE username_us = %s"
        values = (user.balance, user.username_us)
        self.db.cursor.execute(sql, values)
        self.db.mydb.commit()
        print(f"Saldo user {user.username_us} berhasil diperbarui di database.")


    def save_history(self, username_us, description, amount):
        times = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = "INSERT INTO history (username_us, description, amount, timestamp) VALUES (%s, %s, %s, %s)"
        values = (username_us, description, amount, times)
        self.db.cursor.execute(sql, values)
        self.db.mydb.commit()


    def get_history(self, username_us):
        sql = "SELECT description, amount, timestamp FROM history WHERE username_us=%s ORDER BY timestamp DESC"
        self.db.cursor.execute(sql, (username_us,))
        return self.db.cursor.fetchall()

   

import database
import random

def generate_rekening():
    return str(random.randint(100000, 999999))

class datauser:
    def __init__(self, Username_us, Password_us, Balance, Role_us):
        self.No_rek = generate_rekening()
        self.Username_us = Username_us
        self.Password_us = Password_us
        self.Role_us = Role_us
        self.Balance = Balance
    
    def insert_user(self) :
        database.db.cursor.execute(f"INSERT INTO datauser VALUES( '{self.No_rek}','{self.Username_us}','{self.Password_us}','{self.Balance}','{self.Role_us}')")
        database.db.mydb.commit()

        # print("Data sudah masuk")

    def panggil_user(self, Username_us, Password_us):
        database.db.cursor.execute(f"SELECT * FROM datauser WHERE username_us = '{Username_us}' AND password_us = '{Password_us}'")
        returnData = database.db.cursor.fetchone()
        return returnData

#Pemanggilan
Datauser= datauser("Dosen", "dosen123", "0", "admin")
Datauser.insert_user()


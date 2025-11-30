# import database
# import random

# def generate_rekening():
#     return str(random.randint(100000, 999999))

# class datauser:
#     def __init__(self, Username_us, Password_us, Balance, Role_us):
#         self.No_rek = generate_rekening()
#         self.Username_us = Username_us
#         self.Password_us = Password_us
#         self.Role_us = Role_us
#         self.Balance = Balance
    
#     def insert_user(self) :
#         database.db.cursor.execute(f"INSERT INTO datauser VALUES( '{self.No_rek}','{self.Username_us}','{self.Password_us}','{self.Balance}','{self.Role_us}')")
#         database.db.mydb.commit()

#         # print("Data sudah masuk")

#     def panggil_user(self, Username_us, Password_us):
#         database.db.cursor.execute(f"SELECT * FROM datauser WHERE username_us = '{Username_us}' AND password_us = '{Password_us}'")
#         returnData = database.db.cursor.fetchone()
#         return returnData

# #Pemanggilan
# Datauser= datauser("Dosen", "dosen123", "0", "admin")
# Datauser.insert_user()

import database
import random

def generate_rekening():
    return str(random.randint(100000, 999999))

class DataUser:
    def __init__(self,username_us, password_us, balance, role_us):
        self.no_rek = generate_rekening()
        self.username_us = username_us
        self.password_us = password_us
        self.balance = balance
        self.role_us = role_us

    def as_tuple(self):
        return (self.username_us, self.password_us, self.balance, self.role_us)
    
    def insert_user(self):
        query = """
            INSERT INTO datauser (no_rek, username_us, password_us, balance, role_us)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (self.no_rek, self.username_us, self.password_us, self.balance, self.role_us)

        database.db.cursor.execute(query, values)
        database.db.mydb.commit()

        print("User berhasil ditambahkan! Rek:", self.no_rek)
    
    def update_datauser (self):
        sql = f"UPDATE datauser SET username_us = %s,password_us = %s,balance = %s,role_us = %s WHERE no_rek IN(%s)"
        data = (self.username_us,self.password_us,self.balance,self.role_us,self.no_rek)

        update_result = database.execute_sql(sql,data)

class UserRepository:

    def __init__(self):
        self.db = database.db   

    def ambil_user(self):
        sql = "SELECT username_us, password_us, balance, role_us FROM datauser"
        self.db.cursor.execute(sql)
        results = self.db.cursor.fetchall()

        users = []
        for row in results:
            user = DataUser(row[0], row[1], row[2], row[3])
            users.append(user)

        return users

    def panggil_user(self, username, password):
        sql = "SELECT * FROM datauser WHERE username_us = %s AND password_us = %s"
        values = (username, password)
        self.db.cursor.execute(sql, values)
        return self.db.cursor.fetchone()
    
# Pemanggilan
Datauser = DataUser("Dosen", "dosen123", 0, "admin")
# Datauser.insert_user()


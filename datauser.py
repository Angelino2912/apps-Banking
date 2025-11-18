import database


class datauser:
    def __init__(self, nama_costumer, nomor_rekening, saldo_user):
        self.nama_costumer = nama_costumer
        self.nomor_rekening = nomor_rekening
        self.saldo_user = saldo_user
    
    def insert_user(self) :
        database.db.cursor.execute(f"INSERT INTO data_user VALUES( '{self.nama_costumer}','{self.nomor_rekening}','{self.saldo_user}')")
        database.db.mydb.commit()

        print("Data sudah masuk")

    def panggil_user(self, username, paasword):
        database.db.cursor.execute(f"SELECT * FROM user_login WHERE nama_user = '{username}' AND password_user = '{paasword}' ")
        returnData = database.db.cursor.fetchone()
        return returnData



data_user = datauser("Test 1","123456789","0")
data_user.insert_user()



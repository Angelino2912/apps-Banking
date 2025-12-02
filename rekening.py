import database   
from transaksi import Transaksi

# class Rekening:
#     def __init__(self,nomor_rekening):
#         self.nomor_rekening = nomor_rekening

#         self.conn = database.db.mydb
#         self.cursor = self.conn.cursor()

#         query = "SELECT username, saldo FROM rekening WHERE nomor_rekening = %s"
#         self.cursor.execute(query, (self.nomor_rekening,))
#         result = self.cursor.fetchone()

#         if result:
#             self.username = result[0]
#             self.saldo = result[1]
#         else:
#             raise Exception("Nomor rekening tidak ditemukan!")

#     def cek_saldo(self):
#         print(f"Saldo Anda: Rp {self.saldo}")

#     def setor(self, jumlah):
#         if jumlah > 0:
#             self.saldo += jumlah

#             query = "UPDATE rekening SET saldo = %s WHERE nomor_rekening = %s"
#             self.cursor.execute(query, (self.saldo, self.nomor_rekening))
#             self.conn.commit()

#             print(f"Berhasil setor Rp {jumlah}. Saldo baru: Rp {self.saldo}")

#         else:
#             print("Jumlah setor harus lebih dari 0")

#     def tarik(self, jumlah):
#         if jumlah <= 0:
#             print("Jumlah penarikan harus lebih dari 0")
#         elif jumlah > self.saldo:
#             print("Saldo tidak mencukupi")
#         else:
#             self.saldo -= jumlah

#         query = "UPDATE rekening SET saldo = %s WHERE nomor_rekening = %s"
#         self.cursor.execute(query, (self.saldo, self.nomor_rekening))
#         self.conn.commit()

#         print(f"Berhasil tarik Rp {jumlah}. Saldo baru: Rp {self.saldo}")

# # rekening1 = Rekening(637211)

# # rekening1.cek_saldo()
# # rekening1.setor(500000)
# # # rekening1.tarik(300000)
# # rekening1.cek_saldo()

# # rekening2 = Rekening(657709)
# # rekening2.cek_saldo()
# # rekening2.setor(500000)
# # rekening2.cek_saldo()

# rekening3 = Rekening(915437)
# rekening3.cek_saldo()
# rekening3.setor(500000)
# rekening3.cek_saldo()

# rekening.py
# import mysql.connector  # Contoh: MySQL, bisa disesuaikan

class Rekening:
    def __init__(self, nomor_rekening, username, password, saldo, conn):
        self.nomor_rekening = nomor_rekening
        self.username = username
        self.password = password
        self.saldo = saldo
        self.conn = conn
        self.cursor = conn.cursor()

    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            query = "UPDATE rekening SET saldo = %s WHERE nomor_rekening = %s"
            self.cursor.execute(query, (self.saldo, self.nomor_rekening))
            self.conn.commit()
            print(f"Berhasil setor Rp {jumlah}. Saldo baru: Rp {self.saldo}")
        else:
            print("Jumlah setor harus lebih dari 0")

    def tarik(self, jumlah):
        if jumlah <= 0:
            print("Jumlah penarikan harus lebih dari 0")
            return
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi")
            return
        self.saldo -= jumlah
        query = "UPDATE rekening SET saldo = %s WHERE nomor_rekening = %s"
        self.cursor.execute(query, (self.saldo, self.nomor_rekening))
        self.conn.commit()
        print(f"Berhasil tarik Rp {jumlah}. Saldo baru: Rp {self.saldo}")

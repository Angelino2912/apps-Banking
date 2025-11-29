import database   
from transaksi import Transaksi

class Rekening:
    def __init__(self,nomor_rekening):
        self.nomor_rekening = nomor_rekening

        self.conn = database.db.mydb
        self.cursor = self.conn.cursor()

        query = "SELECT username, saldo FROM rekening WHERE nomor_rekening = %s"
        self.cursor.execute(query, (self.nomor_rekening,))
        result = self.cursor.fetchone()

        if result:
            self.username = result[0]
            self.saldo = result[1]
        else:
            raise Exception("Nomor rekening tidak ditemukan!")
    
    def cek_saldo(self):
        print(f"Saldo Anda: Rp {self.saldo}")

    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah

            query = "UPDATE rekening SET saldo = %s WHERE nomor_rekening = %s"
            self.cursor.execute(query, (self.saldo, self.nomor_rekening))
            self.conn.commit()

            user = Transaksi()
            user.catat("SETOR", jumlah, f"Setor ke rekening {self.nomor_rekening}")
            user.tutup()

            print(f"Berhasil setor {jumlah}")

    def tarik(self, jumlah):
        if jumlah <= 0:
            print("Jumlah tidak valid")
            return

        if jumlah > self.saldo:
            print("Saldo tidak cukup")
            return

        self.saldo -= jumlah

        query = "UPDATE rekening SET saldo = %s WHERE nomor_rekening = %s"
        self.cursor.execute(query, (self.saldo, self.nomor_rekening))
        self.conn.commit()

        user = Transaksi()
        user.catat("TARIK", jumlah, f"Tarik dari rekening {self.nomor_rekening}")
        user.tutup()

        print(f"Berhasil tarik Rp {jumlah}. Saldo baru: Rp {self.saldo}")

# rekening1 = Rekening(637211)
# rekening1.cek_saldo()
# rekening1.setor(500000)
# # rekening1.tarik(300000)
# rekening1.cek_saldo()

# rekening2 = Rekening(657709)
# # rekening2.cek_saldo()
# # rekening2.setor(500000)
# # rekening2.cek_saldo()
# rekening2.tarik(300000)

# rekening3 = Rekening(915437)
# rekening3.cek_saldo()
# # # rekening3.setor(500000)
# # rekening3.cek_saldo()
# rekening3.tarik(300000)
                                
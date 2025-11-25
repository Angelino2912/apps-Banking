import database

class Rekening:
    def __init__(self, nomor_rekening, username, saldo=0):
        self.nomor_rekening = nomor_rekening
        self.username = username
        self.saldo = saldo

    def cek_saldo(self):
        print(f"Saldo Anda: Rp {self.saldo}")

    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Berhasil setor Rp {jumlah}. Saldo baru: Rp {self.saldo}")
        else:
            print("Jumlah setor harus lebih dari 0")

    def tarik(self, jumlah):
        if jumlah <= 0:
            print("Jumlah penarikan harus lebih dari 0")
        elif jumlah > self.saldo:
            print("Saldo tidak mencukupi")
        else:
            self.saldo -= jumlah
            print(f"Berhasil tarik Rp {jumlah}. Saldo baru: Rp {self.saldo}")


# ---------------------
# Contoh penggunaan
# ---------------------

rekening1 = Rekening(12345, "angelino", 500000)

rekening1.cek_saldo()
rekening1.setor(250000)
rekening1.tarik(300000)
rekening1.cek_saldo()

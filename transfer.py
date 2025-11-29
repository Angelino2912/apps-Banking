import database
from transaksi import Transaksi

class Transfer:
    def __init__(self, rek_asal, rek_tujuan, jumlah):
        self.rek_asal = rek_asal
        self.rek_tujuan = rek_tujuan
        self.jumlah = jumlah

        self.conn = database.db.mydb
        self.cursor = database.db.cursor

    def proses(self):
        self.cursor.execute(
            "SELECT saldo FROM rekening WHERE no_rek = %s",
            (self.rek_asal,)
        )
        asal = self.cursor.fetchone()

        if not asal:
            print("Rekening asal tidak ditemukan")
            return

        saldo_asal = asal[0]
        if saldo_asal < self.jumlah:
            print("Saldo tidak cukup")
            return

        self.cursor.execute(
            "SELECT saldo FROM rekening WHERE no_rek = %s",
            (self.rek_tujuan,)
        )
        tujuan = self.cursor.fetchone()

        if not tujuan:
            print("Rekening tujuan tidak ditemukan")
            return

        saldo_tujuan = tujuan[0]

        saldo_asal_baru = saldo_asal - self.jumlah
        self.cursor.execute(
            "UPDATE rekening SET saldo = %s WHERE no_rek = %s",
            (saldo_asal_baru, self.rek_asal)
        )

        saldo_tujuan_baru = saldo_tujuan + self.jumlah
        self.cursor.execute(
            "UPDATE rekening SET saldo = %s WHERE no_rek = %s",
            (saldo_tujuan_baru, self.rek_tujuan)
        )

        self.conn.commit()

        Transaksi(
            self.rek_asal, 
            "transfer_keluar", 
            self.jumlah, 
            f"Transfer ke {self.rek_tujuan}"
        ).simpan()

        Transaksi(
            self.rek_tujuan, 
            "transfer_masuk", 
            self.jumlah, 
            f"Transfer dari {self.rek_asal}"
        ).simpan()

        print("✔ Transfer berhasil!")

from rekening import Rekening

rek1 = Rekening(637211)
rek1.transfer_ke(657709, 100000)

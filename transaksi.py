import database

class Transaksi:

    def __init__(self):
        self.conn = database.db.mydb
        self.cursor = database.db.cursor

    def catat(self, tipe, jumlah, keterangan):
        query = """
            INSERT INTO transaksi (tipe, jumlah, keterangan, tanggal)
            VALUES (%s, %s, %s, NOW())
        """
        self.cursor.execute(query, (tipe, jumlah, keterangan))
        self.conn.commit()

        print("Transaksi berhasil dicatat!")

    def tutup(self):
        self.cursor.close()
        self.conn.close()

class Transaksi:
    def __init__(self, no_rek, tipe, jumlah, keterangan):
        self.no_rek = no_rek
        self.tipe = tipe
        self.jumlah = jumlah
        self.keterangan = keterangan
        self.conn = database.db.mydb
        self.cursor = database.db.cursor

    def simpan(self):
        query = """
            INSERT INTO transaksi (no_rek, tipe, jumlah, keterangan, tanggal)
            VALUES (%s, %s, %s, %s, NOW())
        """

        self.cursor.execute(
            query, 
            (self.no_rek, self.tipe, self.jumlah, self.keterangan)
        )
        self.conn.commit()

        print(f"✔ Transaksi disimpan → {self.tipe} | Rek: {self.no_rek}")
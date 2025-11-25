import mysql.connector as mysql_conn

class database:
    def __init__(self):
        self.mydb = mysql_conn.connect(
            host="localhost",
            user="root",
            password = "",
            database="database"
        )
        
        self.cursor = self.mydb.cursor()

db = database()
print(db.mydb)

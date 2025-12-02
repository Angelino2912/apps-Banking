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
    
    def execute_sql(self ,sql, val) :
        self.cursor.execute(sql, val)
        self.mydb.commit()
        return self.cursor.rowcount
    def fetch_data(self ,sql) :
        self.cursor.execute(sql)

        myresult = self.cursor.fetchall()
        return myresult

   
db = database()
print(db.mydb)
    




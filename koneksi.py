
import mysql.connector

def buka_koneksi():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="513649395237",
            database="kos"
        )

        return db

    except mysql.connector.Error as err:
        print("Koneksi database gagal:", err)
        return None


from koneksi import buka_koneksi

def login_admin():
    print("\n========== LOGIN ADMIN ==========")

    username = input("Username: ")
    password = input("Password: ")

    db = buka_koneksi()

    if db is None:
        return False

    cursor = db.cursor()

    sql = """
        SELECT * FROM user
        WHERE username = %s
        AND password = %s
        AND role = 'admin'
    """

    cursor.execute(sql, (username, password))
    admin = cursor.fetchone()

    cursor.close()
    db.close()

    if admin:
        print("\nLogin berhasil!")
        print("Selamat datang,", admin[3])
        return True
    else:
        print("\nLogin gagal!")
        print("Username atau password salah.")
        return False

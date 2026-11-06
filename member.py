
from koneksi import buka_koneksi


def login_member():
    print("\n========== LOGIN MEMBER ==========")

    id_pgh = input("Masukkan ID: ")

    db = buka_koneksi()

    if db is None:
        return

    cursor = db.cursor()

    sql = """
        SELECT
            p.id_pgh,
            p.nama,
            k.nomor_kamar,
            p.masa_sewa
        FROM penghuni p
        JOIN kamar k ON p.id_kmr = k.id_kmr
        WHERE p.id_pgh = %s
    """

    cursor.execute(sql, (id_pgh,))
    data = cursor.fetchone()

    if data:
        print("\n========== DATA PENGHUNI ==========")
        print("ID          :", data[0])
        print("Nama        :", data[1])
        print("Kamar       :", data[2])
        print("Lama Sewa   :", data[3], "Bulan")
        print("==================================")
    else:
        print("\nID Penghuni tidak ditemukan!")

    cursor.close()
    db.close()

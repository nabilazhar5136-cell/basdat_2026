
from koneksi import buka_koneksi


def tampilkan_kamar():
    db = buka_koneksi()

    if db is None:
        return

    cursor = db.cursor()

    sql = """
        SELECT
            k.id_kmr,
            k.nomor_kamar,
            k.kapasitas,
            k.harga_sewa,
            g.nama_gedung,
            COUNT(p.id_pgh) AS jumlah_penghuni
        FROM kamar k
        JOIN gedung g ON k.id_gdg = g.id_gdg
        LEFT JOIN penghuni p ON k.id_kmr = p.id_kmr
        GROUP BY
            k.id_kmr,
            k.nomor_kamar,
            k.kapasitas,
            k.harga_sewa,
            g.nama_gedung
        ORDER BY k.nomor_kamar
    """

    cursor.execute(sql)
    data = cursor.fetchall()

    print("\n========== DATA KAMAR ==========")

    for k in data:
        print("--------------------------------")
        print("ID Kamar       :", k[0])
        print("Nomor Kamar    :", k[1])
        print("Kapasitas      :", k[2])
        print("Harga Sewa     : Rp", k[3])
        print("Gedung         :", k[4])
        print("Jumlah Penghuni:", k[5])

        if k[5] >= k[2]:
            print("Status         : PENUH")
        else:
            print("Status         : TERSEDIA")

    cursor.close()
    db.close()


def menu_kamar():
    while True:
        print("\n========== MENU KAMAR ==========")
        print("1. Lihat Data Kamar")
        print("2. Kembali")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_kamar()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid!")


from koneksi import buka_koneksi


def tampilkan_penghuni():
    db = buka_koneksi()

    if db is None:
        return

    cursor = db.cursor()

    sql = """
        SELECT p.id_pgh, p.nama, p.umur,
               p.tanggal_masuk, p.masa_sewa,
               k.nomor_kamar, g.nama_gedung
        FROM penghuni p
        JOIN kamar k ON p.id_kmr = k.id_kmr
        JOIN gedung g ON k.id_gdg = g.id_gdg
        ORDER BY p.id_pgh
    """

    cursor.execute(sql)
    data = cursor.fetchall()

    print("\n========== DATA PENGHUNI ==========")

    if not data:
        print("Belum ada data penghuni.")
    else:
        for p in data:
            print("----------------------------------")
            print("ID           :", p[0])
            print("Nama         :", p[1])
            print("Umur         :", p[2])
            print("Tanggal Masuk:", p[3])
            print("Masa Sewa    :", p[4], "bulan")
            print("Nomor Kamar  :", p[5])
            print("Gedung       :", p[6])

    cursor.close()
    db.close()


def tambah_penghuni():
    print("\n========== TAMBAH PENGHUNI ==========")

    nama = input("Nama penghuni: ")
    umur = int(input("Umur: "))
    tanggal = input("Tanggal masuk (YYYY-MM-DD): ")
    masa_sewa = int(input("Masa sewa (bulan): "))
    id_kmr = int(input("ID kamar: "))

    db = buka_koneksi()

    if db is None:
        return

    cursor = db.cursor()

    # Periksa kapasitas kamar
    sql_kamar = """
        SELECT kapasitas, nomor_kamar
        FROM kamar
        WHERE id_kmr = %s
    """

    cursor.execute(sql_kamar, (id_kmr,))
    kamar = cursor.fetchone()

    if kamar is None:
        print("Kamar tidak ditemukan!")
    else:
        sql_jumlah = """
            SELECT COUNT(*)
            FROM penghuni
            WHERE id_kmr = %s
        """

        cursor.execute(sql_jumlah, (id_kmr,))
        jumlah = cursor.fetchone()[0]

        if jumlah >= kamar[0]:
            print("Kamar sudah penuh!")
        else:
            sql_insert = """
                INSERT INTO penghuni
                (nama, umur, tanggal_masuk, masa_sewa, id_kmr)
                VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(
                sql_insert,
                (nama, umur, tanggal, masa_sewa, id_kmr)
            )

            db.commit()

            print("\nPenghuni berhasil ditambahkan!")
            print("Nomor kamar:", kamar[1])
            print("Riwayat sewa akan dicatat otomatis oleh Trigger.")

    cursor.close()
    db.close()


def menu_penghuni():
    while True:
        print("\n========== DATA PENGHUNI ==========")
        print("1. Lihat Data Penghuni")
        print("2. Tambah Penghuni")
        print("3. Kembali")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_penghuni()
        elif pilihan == "2":
            tambah_penghuni()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")

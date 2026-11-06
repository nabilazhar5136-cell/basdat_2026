
from koneksi import buka_koneksi


def tampilkan_riwayat():
    db = buka_koneksi()

    if db is None:
        return

    cursor = db.cursor()

    sql = """
        SELECT r.id_pgh, p.nama,
               k.nomor_kamar,
               r.lama_sewa, r.tanggal
        FROM riwayat_sewa r
        JOIN penghuni p ON r.id_pgh = p.id_pgh
        JOIN kamar k ON p.id_kmr = k.id_kmr
        ORDER BY r.tanggal DESC
    """

    cursor.execute(sql)
    data = cursor.fetchall()

    print("\n========== RIWAYAT SEWA ==========")

    if not data:
        print("Belum ada riwayat sewa.")
    else:
        for r in data:
            print("--------------------------------")
            print("ID Penghuni :", r[0])
            print("Nama        :", r[1])
            print("Kamar       :", r[2])
            print("Lama Sewa   :", r[3], "bulan")
            print("Tanggal     :", r[4])

    cursor.close()
    db.close()

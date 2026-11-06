
from login import login_admin
from penghuni import menu_penghuni
from riwayat_sewa import tampilkan_riwayat
from kamar import menu_kamar
from member import login_member

def menu_utama():
    while True:
        print("\n================================")
        print("       SISTEM MANAJEMEN KOS")
        print("================================")
        print("1. Login Admin")
        print("2. Login Member")
        print("3. Keluar")
        print("================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            if login_admin():
                menu_admin()

        elif pilihan == "2":
            login_member()

        elif pilihan == "3":
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid!")


menu_utama()



def menu_admin():
     while True:
        print("\n========== MENU ADMIN ==========")
        print("1. Data Penghuni")
        print("2. Data Kamar")
        print("3. Riwayat Sewa")
        print("4. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_penghuni()

        elif pilihan == "2":
             menu_kamar()
            
        elif pilihan == "3":
             tampilkan_riwayat()
            
        elif pilihan == "4":
            print("Berhasil logout!")
            break

        else:
            print("Pilihan tidak valid!")



menu_utama()
if login_admin():
    menu_admin()
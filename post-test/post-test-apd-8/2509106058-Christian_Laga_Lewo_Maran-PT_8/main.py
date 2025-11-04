import os
from login import buat_akun, login
from menu import *

while True:
    tabel = PrettyTable(["No", "Menu Masuk"])
    tabel.add_row(["1", "Buat akun"])
    tabel.add_row(["2", "Login"])
    tabel.add_row(["3","Keluar"])
    print(tabel)
    try:
        masuk = int(input("Pilih menu masuk: "))
    except ValueError:
        print("input harus angka!!")
        continue
    os.system("cls || clear")

    if masuk == 1:
        buat_akun()

    elif masuk == 2:
        user = login()
        os.system("cls || clear")
        try:
            if user == "admin":
                while True:
                    tabel = PrettyTable(["No", "Menu Admin"])
                    tabel.add_row(["1", "Tampilkan daftar monster"])
                    tabel.add_row(["2", "Tambah monster"])
                    tabel.add_row(["3", "Ubah nama monster"])
                    tabel.add_row(["4", "Ubah deskripsi monster"])
                    tabel.add_row(["5", "Hapus monster"])
                    tabel.add_row(["6", "Keluar"])
                    print(tabel)
                
                    try:
                        pilih = int(input("Pilih menu: "))
                    except ValueError:
                        os.system("cls || clear")
                        print("Input harus angka!")
                        continue
                    os.system("cls || clear")
                    if pilih == 1:
                        tampilkan_monster()
                    elif pilih == 2:
                        tambah_monster(input("Nama: "), input("Deskripsi: "))
                    elif pilih == 3:
                        ubah_nama_monster(input("Nama lama: "), input("Nama baru: "))
                    elif pilih == 4:
                        ubah_deskripsi(input("Nama: "), input("Deskripsi baru: "))
                    elif pilih == 5:
                        hapus_monster(input("Nama monster yang ingin dihapus: "))
                    elif pilih == 6:
                        lihat_komentar()
                    elif pilih == 7:
                        break
                    else:
                        print("Input tidak valid!")

            elif user:
                while True:
                    tabel = PrettyTable(["No", "Menu Pengunjung"])
                    tabel.add_row(["1", "Lihat monster"])
                    tabel.add_row(["2", "Keluar"])
                    print(tabel)

                    try:
                        pilih = int(input("Pilih menu: "))
                    except ValueError:
                        os.system("cls || clear")
                        print("Input harus angka!")
                        continue
                    os.system("cls || clear")
                    
                    if pilih == 1:
                        tampilkan_monster()
                    elif pilih == 2:
                        tambah_komentar()
                    elif pilih == 3:
                        print("Terima kasih!")
                        break
                    else:
                        print("Input tidak valid!")
        except ValueError:
            print("input yang anda masukkan bukan Integer (angka)")


    elif masuk == 3:
        print("Program selesai.")
        break

    else:
        print("Menu tidak valid!")

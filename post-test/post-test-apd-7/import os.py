import os
os.system("cls || clear")

users = {
    "admin": "admin123"
}

monstermusuh = {
    "evil_warriors": "prajurit kerajaan yang terkontaminasi energi kegelapan dan kehilangan kendali akan dirinya",
    "skeleton_army": "sekumpulan pasukan yang dibangkitkan dari kematian tetapi hanya dalam bentuk kerangka tengkorak",
    "bounty_hunter": "pemburu orang bayaran",
    "undead_cavalry": "pasukan berkuda yang dibangkitkan dari kematian",
    "river_reaver": "sekelompok penjarah yang beraksi di daerah sungai",
    "deep_sea_titan": "makhluk raksasa yang tertidur di dasar lautan"
}

border = "-" * 40

def buat_akun():
        username = input("Buat username: ")
        password = input("Buat password: ")
        if username in users:
            print("Username sudah ada!")
        else:
            users[username] = password
            print("Akun berhasil dibuat!")

def tampilkan_monster():
    print(border)
    print("Daftar Monster dan Musuh:")
    print(border)
    for i, j in monstermusuh.items():
        print(f"{i} :\n{j}\n")

def tambah_monster(nama, deskripsi):
    if nama in monstermusuh:
        print("Monster atau musuh sudah ada.")
    else:
        monstermusuh[nama] = deskripsi
        print(f"berhasil menambahkan", {nama})

def ubah_deskripsi(nama, deskripsi_baru):
    try:
        if nama in monstermusuh:
            monstermusuh[nama] = deskripsi_baru
            print(f"Deskripsi {nama} berhasil diperbarui!")
    except KeyError:
        print("Monster tidak ditemukan dalam daftar")
        
def hapus_monster():
    try:
        hapus = input("Masukkan nama monster/musuh yang ingin dihapus: ")
        if hapus in monstermusuh:
            monstermusuh.pop(hapus)
            print(f"{hapus} berhasil dihapus!")
    except KeyError:
        print("Monster tidak ditemukan dalam daftar")

while True:
    print(border)
    print("""1. Buat akun
2. Login
3. Keluar""")
    print(border)
    masuk = input("Pilih menu masuk: ")

    os.system("cls || clear")

    if masuk == "1":
        buat_akun()

    elif masuk == "2":
        usrnm = input("Masukkan username: ")
        psswrd = input("Masukkan password: ")

        try:
            if usrnm in users and psswrd == users[usrnm]:
                os.system("cls || clear")

                if usrnm == "admin":
                    while True:
                        print(border)
                        print("""Menu Admin
1. Tampilkan daftar monster
2. Tambah monster
3. Ubah deskripsi monster
4. Hapus monster
5. Keluar""")
                        print(border)
                        pilih = int(input("Pilih menu: "))
                        os.system("cls || clear")

                        if pilih == 1:
                            tampilkan_monster()
                        elif pilih == 2:
                            nama = input("Masukkan nama monster: ")
                            deskripsi = input("Masukkan deskripsi: ")
                            tambah_monster(nama, deskripsi)
                        elif pilih == 3:
                            nama = input("Masukkan nama monster: ")
                            deskripsi_baru = input("Masukkan deskripsi baru: ")
                            ubah_deskripsi(nama, deskripsi_baru)
                        elif pilih == 4:
                            hapus_monster()
                        elif pilih == 5:
                            print("Kembali ke menu utama...")
                            break
                        else:
                            print("Input tidak valid!")

                else:
                    while True:
                        print(border)
                        print("""Menu Pengunjung
1. Lihat daftar monster
2. Keluar""")
                        print(border)
                        pilihan = int(input("Pilih menu: "))
                        os.system("cls || clear")

                        if pilihan == 1:
                            tampilkan_monster()
                        elif pilihan == 2:
                            print("Terima kasih atas kunjungannya!")
                            break
                        else:
                            print("Input tidak valid!")
            else:
                print("Username atau password salah!")
        except ValueError:
            print("print(input yang anda masukkan bukan Integer (angka)")

    elif masuk == "3":
        print("Program selesai. Sampai jumpa lagi!")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")

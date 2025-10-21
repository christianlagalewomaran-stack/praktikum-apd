import os
os.system('cls' if os.name == 'nt' else 'clear')

users = {
    "admin" : "admin123"
}

monstermusuh = {
    "evil_warriors" : "prajurit kerajaan yang terkontaminasi energi kegelapan dan kehilangan kendali akan dirinya", 
    "skeleton_army" : "sekumpulan pasukan yang dibangkitkan dari kematian tetapi hanya dalam bentuk kerangka tengkorak", 
    "bounty_hunter" : "pemburu orang bayaran",
    "undead_cavalry" : "pasukan berkuda yang dibangkitkan dari kematian", 
    "river_reaver" : "sekolompok penjarah yang beraksi di daerah sungai",
    "deep_sea_titan" : "makhluk raksasa yang tertidur di dasar lautan"
}

border = "-"*40

while True:
    print (border)
    print("""1.buat akun
2.Login
3.Keluar""")
    print(border)
    masuk = (input("pilih menu masuk: "))
    if masuk == "1":
            username = input("Buat username: ")
            password = input("Buat password: ")
            if username in users:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Username sudah ada, coba yang lain!")
            else:
                users.update({username : password})
                os.system('cls' if os.name == 'nt' else 'clear')
                print ("akun berhasil dibuat")
    elif masuk == "2":
            usrnm = input("Masukkan username: ")
            psswrd = input("Masukkan password: ")
            if usrnm in users and psswrd == users[usrnm]:
                os.system('cls' if os.name == 'nt' else 'clear')
                if usrnm == "admin" and psswrd == users["admin"]:
                    while True:
                        print(border)
                        print ("""menu admin
1.Tampilkan daftar monster dan musuh
2.Tambah daftar monster dan musuh
3.Ubah daftar monster dan musuh
4.Ubah deskripsi monster dan musuh
5.hapus daftar monster dan musuh
6.keluar""")
                        print(border)
                        pilih = (input("pilih menu: "))
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if pilih == "1":
                            for i, j in monstermusuh.items():
                                print(f" {i} : \n {j}")
                                print()
                        elif pilih == "2":
                            plusmm = (input("masukan nama monster atau musuh: "))
                            if plusmm in monstermusuh:
                                print("monster atau musuh sudah tersedia")
                            else:
                                dskrpsi = (input("masukan deskripsi: "))
                                monstermusuh.update({plusmm : dskrpsi })
                                print("berhasil menambahkan", plusmm)
                                
                        elif pilih == "3":
                            pembaruan = (input("pilih monster atau musuh: "))
                            if pembaruan in monstermusuh:
                                perbarui = (input("perbarui monster atau musuh: "))
                                monstermusuh[perbarui] = monstermusuh.pop(pembaruan)
                                print ("berhasil mengubah", pembaruan, "menjadi", perbarui)
                            else:
                                print ("monster atau musuh tidak ditemukan")
                                
                        elif pilih == "4":
                            plhdskrpsi = (input("pilih monster atau musuh: "))
                            if plhdskrpsi in monstermusuh:
                                updtdskrpsi = (input("silahkan perbarui deskripsi monster atau musuh yang dipilih: "))
                                monstermusuh[plhdskrpsi] = updtdskrpsi
                                print ("berhasil mengubah deskripsi", plhdskrpsi)
                            else:
                                print ("monster atau musuh tidak ditemukan")
                                
                        elif pilih =="5":
                            hapus = (input("pilih monster atau musuh yang akan di hapus: "))
                            if  hapus in monstermusuh:
                                monstermusuh.pop(hapus)
                                print ("berhasil menghapus",hapus)
                            else:
                                print("monster atau musuh tidak ditemukan")
                                
                        elif pilih =="6":
                            print ("kembali ke menu")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                        
                        else:
                            print ("tidak valid, pilih ulang")
                            
                else:
                    while True:
                        print(border)
                        print ("""menu pengunjung
1.lihat daftar monster dan musuh
2.keluar""")
                        print(border)
                        pilihan = (input("pilih menu: "))
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if pilihan == "1":
                            for i, j in monstermusuh.items():
                                print(f" {i} : \n {j}")
                                print()
                        elif pilihan == "2":
                            print("Terima Kasih atas kunjungannya sampai jumpa lagi")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                        
                        else:
                            print ("tidak valid, pilih ulang")
                
            else:
                print("username atau password salah, coba lagi")
                
    elif masuk == "3":
        print ("program selesai")
        break
    
    else:
        print ("tidak valid, coba lagi")
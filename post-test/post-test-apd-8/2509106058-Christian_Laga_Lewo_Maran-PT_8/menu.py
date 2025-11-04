from prettytable import PrettyTable

monstermusuh = {
    "evil_warriors": "prajurit kerajaan yang terkontaminasi energi kegelapan dan kehilangan kendali akan dirinya",
    "skeleton_army": "sekumpulan pasukan yang dibangkitkan dari kematian tetapi hanya dalam bentuk kerangka tengkorak",
    "bounty_hunter": "pemburu orang bayaran",
    "undead_cavalry": "pasukan berkuda yang dibangkitkan dari kematian",
    "river_reaver": "sekelompok penjarah yang beraksi di daerah sungai",
    "deep_sea_titan": "makhluk raksasa yang tertidur di dasar lautan"
}

komentar_pengunjung = {}

def tampilkan_monster():
    table = PrettyTable()
    table.field_names = ["Nama Monster", "Deskripsi"]
    for nama, desk in monstermusuh.items():
        table.add_row([nama, desk])
    print(table)

def tambah_monster(nama, deskripsi):
    if nama in monstermusuh:
        print("Monster sudah ada!")
    else:
        monstermusuh[nama] = deskripsi
        print(f"{nama} berhasil ditambahkan!")

def ubah_nama_monster(nama_lama, nama_baru):
    if nama_lama in monstermusuh:
        monstermusuh[nama_baru] = monstermusuh.pop(nama_lama)
        print(f"Nama monster berhasil diubah dari {nama_lama} menjadi {nama_baru}")
    else:
        print("Monster tidak ditemukan!")

def ubah_deskripsi(nama, deskripsi_baru):
    if nama in monstermusuh:
        monstermusuh[nama] = deskripsi_baru
        print(f"Deskripsi {nama} berhasil diperbarui!")
    else:
        print("Monster tidak ditemukan!")

def hapus_monster(nama):
    if nama in monstermusuh:
        monstermusuh.pop(nama)
        print(f"{nama} berhasil dihapus!")
    else:
        print("Monster tidak ditemukan!")

def tambah_komentar():
    nama = input("Masukkan nama Anda: ")
    masukan = input("Masukkan komentar / feedback: ")

    komentar_pengunjung[nama] = masukan

    print("Terima kasih, komentar berhasil ditambahkan!")
    
def lihat_komentar():
    if len(komentar_pengunjung) == 0:
        print("Belum ada komentar.")
    else:
        for nama, isi in komentar_pengunjung.items():
            print(f"{nama} : {isi}")

    

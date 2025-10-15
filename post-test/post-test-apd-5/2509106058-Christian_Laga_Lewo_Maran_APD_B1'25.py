import os
os.system('cls' if os.name == 'nt' else 'clear')

users = ["admin"]
pw = ["user01"]
monstermusuh = ["evil_warriors", "skeleton_army", "bounty_hunter","undead_cavalry", "river_reaver","deep_sea_titan"]
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
			print("Username sudah ada, coba yang lain!")
		else:
			users.append(username)
			pw.append(password)
			print ("akun berhasil dibuat")
	elif masuk == "2":
		usrnm = input("Masukkan username: ")
		psswrd = input("Masukkan password: ")
		if usrnm in users and psswrd in pw:
			y = users.index(usrnm)
			if pw[y] == psswrd:
				print ("login berhasil")
				os.system('cls' if os.name == 'nt' else 'clear')
				if usrnm == "admin" and psswrd == "user01":
					while True:
						print(border)
						print ("""menu admin
1.Tampilkan daftar monster dan musuh
2.Tambah daftar monster dan musuh
3.Ubah daftar monster dan musuh
4.hapus daftar monster dan musuh
5.keluar""")
						print(border)
						pilih = (input("pilih menu: "))
						if pilih == "1":
							for x in monstermusuh:
								print ("\n", x, "\n")
						elif pilih == "2":
							plusmm = (input("masukan nama monster atau musuh: "))
							
							if plusmm in monstermusuh:
								print("monster atau musuh sudah tersedia")
							else:
								monstermusuh.append(plusmm)
								print("berhasil menambahkan", plusmm)
			
						elif pilih == "3":
							pembaruan = (input("pilih monster atau musuh: "))
							if pembaruan in monstermusuh:
								x = monstermusuh.index(pembaruan)
								monstermusuh[x] == (input("perbarui monster atau musuh: "))
							else:
								print ("monster atau musuh tidak ditemukan")
								
						elif pilih =="4":
							hapus = (input("pilih monster atau musuh yang akan di hapus: "))
							if  hapus in monstermusuh:
								monstermusuh.remove(hapus)
								print ("berhasil menghapus monster atau musuh")
							else:
								print("monster atau musuh tidak ditemukan")
								
						elif pilih =="5":
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
						if pilihan == "1":
							for x in monstermusuh:
									print ("\n", x, "\n")
						elif pilihan == "2":
							print("Terima Kasih atas kunjungannya sampai jumpa lagi")
							os.system('cls' if os.name == 'nt' else 'clear')
							break
						else:
							print ("tidak valid, pilih ulang")
							
			else:
				print("password salah")
		else:
			print ("login gagal, ulangi")
		
	elif masuk == "3":
		print ("program selesai")
		break
		
	else:
		print ("tidak valid, coba lagi")
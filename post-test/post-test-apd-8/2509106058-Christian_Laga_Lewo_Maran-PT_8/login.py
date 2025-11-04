users = {
    "admin": "admin123"
}

def buat_akun():
    username = input("Buat username: ")
    password = input("Buat password: ")
    if username in users:
        print("Username sudah ada!")
    else:
        users[username] = password
        print("Akun berhasil dibuat!")

def login():
    usrnm = input("Masukkan username: ")
    psswrd = input("Masukkan password: ")
    if usrnm in users and users[usrnm] == psswrd:
        return usrnm
    else:
        print("Login gagal! Username atau password salah.")
        return None

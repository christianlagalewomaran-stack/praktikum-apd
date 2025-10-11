username = input("Masukkan username: ")
while username != "Tian":
    print("Username salah")
    username = input("Masukkan username: ")

password = input("Masukkan password: ")
while password != "058":
    print("Password salah")
    password = input("Masukkan password: ")

A_pos = 0
A_neg = 0
B_pos = 0
B_neg = 0
AB_pos = 0
AB_neg = 0
O_pos = 0
O_neg = 0

ulang = "Y"
while ulang == "Y":
    golongan = input("Masukkan golongan darah: ")

    if golongan == "A":
        Rhesus = input("Masukkan Rhesus")
        if Rhesus == "+":
            print("Golongan darah A+")
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            A_pos = A_pos + (jumlah * 500)
        elif Rhesus == "-":
            print("Golongan darah A-")
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            A_neg = A_neg + (jumlah * 500)
        else:
            print("Rhesus tidak valid")

    elif golongan == "B":
        Rhesus = input("Masukkan Rhesus")
        if Rhesus == "+":
            print("Golongan darah B+")
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            B_pos = B_pos + (jumlah * 500)
        elif Rhesus == "-":
            print("Golongan darah B-")
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            B_neg = B_neg + (jumlah * 500)
        else:
            print("Rhesus tidak valid")

    elif golongan == "AB":
        Rhesus = input("Masukkan Rhesus")
        if Rhesus == "+":
            print("Golongan darah AB+")
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            AB_pos = AB_pos + (jumlah * 500)
        elif Rhesus == "-":
            print("Golongan darah AB-")
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            AB_neg = AB_neg + (jumlah * 500)
        else:
            print("Rhesus tidak valid")

    elif golongan == "O":
        Rhesus = input("Masukkan Rhesus")
        if Rhesus == "+":
            print("Golongan darah O+")
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            O_pos = O_pos + (jumlah * 500)
        elif Rhesus == "-":
            print("Golongan darah O-")
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            O_neg = O_neg + (jumlah * 500)
        else:
            print("Rhesus tidak valid")

    else:
        print("Golongan darah tidak valid")

    ulang = input("Apakah anda masih mau input lagi (Y/T)? ")
    
    while ulang != "T":
        print("isi input hanya dengan Y/T")
        ulang = input("Apakah anda masih mau input lagi (Y/T)? ")

print("\nRingkasan jumlah darah (ml):")
print("A+ :", A_pos, "ml")
print("A- :", A_neg, "ml")
print("B+ :", B_pos, "ml")
print("B- :", B_neg, "ml")
print("AB+:", AB_pos, "ml")
print("AB-:", AB_neg, "ml")
print("O+ :", O_pos, "ml")
print("O+ :", O_neg, "ml")
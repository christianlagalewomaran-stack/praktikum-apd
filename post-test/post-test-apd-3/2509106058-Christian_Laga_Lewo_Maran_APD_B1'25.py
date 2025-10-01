
username = str (input("masukan username"))
password = str (input("masukan password"))
if username == "Tian" and password == "058":
    if password == "058":
        print ("Berhasil login")
        print ("""Konversi panjang ketik 1
Konversi massa ketik 2
Konversi suhu ketik 3
Konversi waktu ketik 4
Konversi mata uang ketik 5""")
    kalkulator = int (input("pilih kalkulator"))
    if kalkulator ==1:
        print ("Konversi satuan panjang ke meter")
        panjang = float (input ("masukan nilai panjang"))
        print ("""ketik 1 untuk satuan kaki (feet)
ketik 2 untuk satuan kilometer
ketik 3 untuk satuan centimeter""")
        satuan_panjang = int (input("masukan satuan panjang"))
        if satuan_panjang == 1:
            panjang *= 0.3048
            print (panjang )
        elif satuan_panjang == 2:
            panjang *= 1000
            print (panjang)
        elif satuan_panjang == 3:
            panjang /= 100
            print (panjang)
        else:
            print ("not found")
            
    elif kalkulator ==2:
        print ("Konversi satuan massa ke kilogram")
        massa = float (input("masukan nilai massa"))
        print ("""ketik 1 untuk satuan pon (pound)
ketik 2 untuk satuan ton
ketik 3 untuk satuan gram
ketik 4 untuk satuan kuintal
ketik 5 untuk satuan stone""")
        satuan_massa = int (input("masukan satuan massa"))
        if satuan_massa == 1:
            massa *= 0.454
            print (massa)
        elif satuan_massa == 2:
            massa *=1000
            print (massa)
        elif satuan_massa == 3:
            massa /= 1000
            print (massa)
        elif satuan_massa == 4:
            massa *= 100
            print (massa)
        elif satuan_massa == 5:
            massa *= 6.35
            print (massa)
        else:
            print ("not found")
            
    elif kalkulator == 3:
        print ("Konversi satuan suhu ke Kelvin")
        suhu = float (input("masukan nilai suhu"))
        print ("""ketik 1 untuk satuan Celcius)
ketik 2 untuk satuan Fahrenheit 
ketik 3 untuk satuan Reamur""")
        satuan_suhu = int (input("masukan satuan suhu"))
        if satuan_suhu == 1:
            suhu += 273.5
            print (suhu)
        elif satuan_suhu == 2:
            suhu += 459.67
            suhu *= 5/9
            print (suhu)
        elif satuan_suhu == 3:
            suhu /= 1000
            print (suhu)
        else:
            print ("not found")
            
    elif kalkulator ==4:
        print ("Konversi satuan waktu ke detik")
        waktu = float (input("masukan nilai waktu"))
        print ("""ketik 1 untuk satuan menit
ketik 2 untuk satuan jam""")
        satuan_waktu = int (input("masukan satuan waktu"))
        if satuan_waktu == 1:
            waktu *= 60
            print (waktu)
        elif satuan_waktu == 2:
            waktu *=3600
            print (waktu)
        else:
            print ("not found")
        
    elif kalkulator ==5:
        print ("Konversi mata uang")
        nilai_mata_uang = float (input("masukan nilai mata uang"))
        print ("""ketik 1 untuk konversi rupiah ke dolar
ketik 2 untuk konversi dolar ke rupiah
ketik 3 untuk konversi ringgit ke rupiah
ketik 4 untuk konversi rupiah ke ringgit
ketik 5 untuk konversi dolar ke euro
ketik 6 untuk konversi euro ke dolar""")
        mata_uang = int (input("masukan pilihan konversi"))
        if mata_uang == 1:
            nilai_mata_uang /= 16670
            print (nilai_mata_uang)
        elif mata_uang == 2:
            nilai_mata_uang *=16670
            print (nilai_mata_uang)
        elif mata_uang == 3:
            nilai_mata_uang *= 3955.64
            print (nilai_mata_uang)
        elif mata_uang == 4:
            nilai_mata_uang /=3955.64
            print (nilai_mata_uang)
        elif mata_uang == 5:
            nilai_mata_uang /= 0.85
            print (nilai_mata_uang)
        elif mata_uang == 6:
            nilai_mata_uang *= 0.85
            print (nilai_mata_uang)
        else:
            print ("not found")
            
    else:
        print ("Not found")
        
elif username == "Tian" and password != "058":
    print ("password salah tapi username benar")
else:
    print ("kesalahan username saja")
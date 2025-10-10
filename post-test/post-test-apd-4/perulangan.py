username = (input("masukan username"))
while username != "Tian":
    print ("username salah")
    username = (input("masukan username"))
password = (input("masukan password"))
while password != "058":
    print ("password salah")
    username = (input("masukan password"))

golongan_darah = (input("golongan darah"))
if golongan_darah == ("A"):
    Rhesus = (input("pilih Rhesus"))
    if Rhesus == ("+"):
        print ("golongan darah A+")
    elif Rhesus == ("-"):
        print ("golongan darah A-")
    else:
        print ("tidak valid")
        
elif golongan_darah == ("B"):
    Rhesus = (input("pilih Rhesus"))
    if Rhesus == ("+"):
        print ("golongan darah B+")
    elif Rhesus == ("-"):
        print ("golongan darah B-")
    else:
        print ("tidak valid")
        
elif golongan_darah == ("C"):
    Rhesus = (input("pilih Rhesus"))
    if Rhesus == ("+"):
        print ("golongan darah C+")
    elif Rhesus == ("-"):
        print ("golongan darah C-")
    else:
        print ("tidak valid")
        
elif golongan_darah == ("O"):
    Rhesus = (input("pilih Rhesus"))
    if Rhesus == ("+"):
        print ("golongan darah O+")
    elif Rhesus == ("-"):
        print ("golongan darah O-")
    else:
        print ("tidak valid")
        
elif golongan_darah == ("AB"):
    Rhesus = (input("pilih Rhesus"))
    if Rhesus == ("+"):
        print ("golongan darah AB+")
    elif Rhesus == ("-"):
        print ("golongan darah AB-")
    else:
        print ("tidak valid")
        
else:
    golongan_darah = "tidak valid"
    while golongan_darah == "tidak valid":
        golongan_darah = (input("golongan darah"))
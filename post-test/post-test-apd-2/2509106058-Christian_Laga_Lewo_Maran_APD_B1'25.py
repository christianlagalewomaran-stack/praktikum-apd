suhu = [27, 33, 46, 55, 67, 92]

suhu_1 = 9/5 * suhu[0] + 32
suhu_2 = 9/5 * suhu[1] + 32
suhu_3 = suhu[-4] + 273.5
suhu_4 = suhu[-3] + 273.5
suhu_5 = 4/5 * suhu[-2] 
suhu_6 = 4/5 * suhu[-1]
NIM = 58
jumlah = suhu_1+suhu_2+suhu_3+suhu_4+suhu_5+suhu_6

bd = len(suhu)
rata_rata = jumlah/bd
boolean = NIM < rata_rata

print(suhu_1)
print(suhu_2)
print(suhu_3)
print(suhu_4)
print(suhu_5)
print(suhu_6)
print(NIM)
print(jumlah)
print(bd)
print(rata_rata)
print(boolean)
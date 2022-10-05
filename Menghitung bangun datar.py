print("menghitung luas Bangun datar")
print("Mari menghitung luas bangun datar")
print("tekan angka 1 untuk persegi")
print("tekan angka 2 untuk segitiga")
print("tekan angka 3 untuk lingkaran")
print("tekan angka 4 untuk Trapesium")
print("tekan angka 5 untuk layang-layang")
print("tekan angka 6 untuk belah ketupat")
print("tekan angka 7 untuk Persegi panjang")
pilihanBangunDatar = int(input())
persegi = 1
segitiga = 2
lingkaran = 3
trapesium = 4
layangLayang = 5
belahKetupat = 6
persegiPanjang = 7

if pilihanBangunDatar == persegi:
    print("berapa sisi persegi")
    sisi = input()
    print("luas perseginya adalah")
    luas =  int(sisi) ** 2
    print(luas)
if pilihanBangunDatar == segitiga:
    print("berapa alas segitiga")
    alas = input()
    print("berapa tinggi segitiga")
    tinggi = input()
    print("luas segitiga adalah")
    luas = 1/2 * int(alas) * int(tinggi)
    print(luas)
if pilihanBangunDatar == lingkaran:
    print("berapa jari-jari lingkaran")
    jariJari = input()
    habis7 = int(jariJari) % 7
    if habis7 == 0: 
        print("luas lingkaran adalah")
        luas = 22/7 * int(jariJari) ** 2
        print(luas)
    else:
        print("luas lingkaran adalah")
        luas = 3.14 * int(jariJari) ** 2
        print(luas)
if pilihanBangunDatar == trapesium:
    print("berapa sisi alas trapesium")
    alas = input()
    print("berapa sisi atas trapesium")
    atas = input()
    print("berapa tinggi trapesium")
    tinggi = input()
    print("luas trapesium adalah")
    luas = 1/2 * (int(alas) + int(atas)) * int(tinggi)
    print(luas)
if pilihanBangunDatar == layangLayang:
    print("berapa diagonal 1 layang - layang")
    diagonal1 = input()
    print("berapa diagonal 2 layang - layang")
    diagonal2 = input()
    print("luas layang - layang adalah")
    luas = 1/2 * int(diagonal1) * int(diagonal2)
    print(luas)
if pilihanBangunDatar == belahKetupat:
    print("berapa diagonal 1 belah ketupat")
    diagonal1 = input()
    print("berapa diagonal 2 belah ketupat")
    diagonal2 = input()
    print("luas layang - layang adalah")
    luas = 1/2 * int(diagonal1) * int(diagonal2)
    print(luas)
if pilihanBangunDatar == persegiPanjang:
    print("berapa panjang persegi panjang")
    panjang = input()
    print("berapa lebar persegi panjang")
    lebar = input()
    print("luas persegi panjang adalah")
    luas = int(panjang) * int(lebar)
    print(luas)
else :
    print("Tolong hanya input angka yang tertera")
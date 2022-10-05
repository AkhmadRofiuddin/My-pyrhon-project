import random

print("=====Selamat Bermain Tebak angka=====")
print("Tebak angka yang benar dari angka satu sampai sepuluh")
angka = random.randint(1,100)
while True:
    for percobaan in range(100):
        angka_tebakan = int(input(f'\n Masukkan angka: '))
        percobaan += 1
        if angka_tebakan > angka:
            print("angka terlalu besar")
        if angka_tebakan < angka:
            print("angka terlalu kecil")
        if angka_tebakan == angka:
            print("Selamat tebakan anda benar pada tebakan ke: " + str(percobaan))
            break
        


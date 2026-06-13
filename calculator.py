def tambah(angkaUser, angkaUser2):
    return angkaUser + angkaUser2
def kurang(angkaUser, angkaUser2):
    return angkaUser - angkaUser2
def kali(angkaUser, angkaUser2):
    return angkaUser * angkaUser2
def bagi(angkaUser, angkaUser2):
    return angkaUser / angkaUser2

angkaUser = int(input('Masukkan angkamu : '))
angkaUser2 = int(input('Masukkan angka kedua : '))

operasi = int(input('Pilih operasi yang diinginkan : \n1. Tambah \n2. Kurang \n3. Kali \n4. Bagi \n Masukkan pilihanmu : '))
while operasi < 1 or operasi > 4:
    operasi = int(input('Pilihan tidak valid, silakan pilih antara 1-4 : '))

if operasi == 1:
    print(f'Hasilnya adalah : {tambah(angkaUser, angkaUser2)}')

elif operasi == 2:
    print(f'Hasilnya adalah : {kurang(angkaUser, angkaUser2)}')

elif operasi == 3:
    print(f'Hasilnya adalah : {kali(angkaUser, angkaUser2)}')

elif operasi == 4:
    while angkaUser2 == 0:
        print('Error: Pembagian dengan nol tidak diperbolehkan. Silakan masukkan angka kedua yang bukan nol.')
        angkaUser2 = int(input('Masukkan angka kedua : '))

    print(f'Hasilnya adalah : {bagi(angkaUser, angkaUser2)}')

else:
    print('Pilihan tidak valid, silakan pilih antara 1-4')
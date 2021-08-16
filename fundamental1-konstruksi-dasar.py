# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL: Eksekusi berurutan
print('Hello World!')
print('by Ade')
print('Tanggal 16 Agustus 2021')
print('-' * 10)

# PERCABANGAN : Eksekusi terpilih
ingin_cepat = True

if ingin_cepat:
    print("Jalan lurus aja!!")
else:
    print("Jalan lain")

# PERCABANGAN PILIHAN LEBIH DARI 2
ingin_balik = True

#PERULANGAN
jumlah_anak = 4

for index_anak in range(1, jumlah_anak+1):
    print(f"Hallo anak {index_anak}")
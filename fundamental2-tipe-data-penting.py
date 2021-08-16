# Tipe data skalar => tipe data sederhana
anak1 = "Eko"
anak2 = "Dwi"
anak3 = "Tri"
anak4 = "Catur"

print(anak1)
print(anak2)
print(anak3)
print(anak4)

# TIPE DATA LIST/DAFTAR/ARRAY
anak = ["Eko", "Dwi", "Tri", "Catur"]
print(anak)
anak.append("Limo")
print(anak)

#SAPA ANAK KE-2
print(f"Hai {anak[1]}!\n")

#SAPA SEMUA ANAK
for a in anak:
    print(f"Hai {a}!!")
print("\n")
# SAPA SEMUA ANAK CARA RIBET
for a in range(0, len(anak)):
    print(f"{a+1}.Hai anak ke-{anak[a]}")
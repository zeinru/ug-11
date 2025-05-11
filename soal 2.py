angka = []

while True:
    masuk = input("Masukkan angka (atau ketik 'done' untuk selesai): ")
    if masuk.lower() == 'done':
        break
    try:
        nilai = float(masuk)
        angka.append(nilai)
    except ValueError:
        print("Input tidak valid. Masukkan angka atau 'done'.")

if angka:
    rata_rata = sum(angka) / len(angka)
    print("Rata-rata dari angka yang dimasukkan adalah:", rata_rata)
else:
    print("Tidak ada angka yang dimasukkan.")

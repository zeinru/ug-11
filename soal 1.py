def tiga_terbesar(data):
   
    data_terurut = sorted(data, reverse=True)
    
    return data_terurut[:3]

angka = [80, 92, 75, 60, 99, 85, 77]
hasil = tiga_terbesar(angka)
print("Tiga angka terbesar adalah:", hasil)

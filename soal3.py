with open("artikel.txt", "r", encoding="utf-8") as file:
    isi = file.read()

kata_kata = isi.lower().split()

import string
kata_bersih = [kata.strip(string.punctuation) for kata in kata_kata]

kata_unik = set(kata_bersih)

print("Kata-kata unik dalam artikel:")
for kata in sorted(kata_unik):
    print(kata)

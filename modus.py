data = [0, 0, 1, 2, 2, 4, 5]
frekuensi = {}
for nilai in data:
    frekuensi[nilai] = frekuensi.get(nilai, 0) + 1
modus = max(frekuensi, key=frekuensi.get)
print("Modus dari himpunan data adalah:", modus)

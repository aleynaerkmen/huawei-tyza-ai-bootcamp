notlar = []
hata_sayisi = 0

with open("notlar.txt", "r", encoding="utf-8") as dosya:

    for satir in dosya:

        try: 
            not_degeri = int(satir.strip())
            notlar.append(not_degeri)
        except ValueError:
            print(f"Hatalı veri bulundu: {satir.strip()}")
            hata_sayisi += 1

print(f"notlar: {notlar}")
print(f"hata_sayisi: {hata_sayisi}")

ortalama = sum(notlar) / len(notlar)

print(f"ortalama: {ortalama}")
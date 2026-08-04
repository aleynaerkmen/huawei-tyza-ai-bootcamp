
with open("notlar.txt", "w", encoding="utf-8") as dosya:
    dosya.write("70\n")
    dosya.write("85\n")
    dosya.write("90\n")
    dosya.write("45\n")
    dosya.write("75\n")

notlar = [] 

with open("notlar.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        notlar.append(int(satir.strip()))

ortalama = sum(notlar) / len(notlar)
en_yuksek = max(notlar)
en_dusuk= min(notlar)

print("Notlar:", notlar)
print("Ortalama:", ortalama)
print("En yüksek not:", en_yuksek)
print("En düşük not:", en_dusuk)

if ortalama >= 50:
    sonuc = "Sınıf geçti"
else:
    sonuc = "Sınıf kaldı"

with open("notlar.txt", "w", encoding="utf-8") as dosya:
    dosya.write(f"Ortalama: {ortalama}\n")
    dosya.write(f"Sonuç: {sonuc}")

print("Sonuç dosyaya kaydedildi.")
  

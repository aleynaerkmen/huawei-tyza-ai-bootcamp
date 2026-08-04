veri = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Ahmet", "Elif"],
    "yas": [25, 30, 28, 35, 22, 27],
    "sehir": ["Ankara", "İstanbul", "Ankara", "İzmir", "Bursa", "İstanbul"],
    "maas": [5000, 7000, 6000, 8000, 4500, 6500]
}

df = pd.DataFrame(veri)
print("VERİ SETİ")
print(df)

# 1. soru
print("SORU 1 CEVAP")
print(df.head(3))

# 2.soru
print("SORU 2 CEVAP")
print(df.columns)

# 3. soru
print("SORU 3 CEVAP")
print(df["isim"])

# 4. soru
print("SORU 4 CEVAP")
print(df[["isim", "maas"]])

# 5. soru
print("SORU 5 CEVAP")
print(df[df["yas"] > 28])

# 6. soru
print("SORU 6 CEVAP")
print(df[df["maas"] > 6000][["isim", "maas"]])

# 7. soru
print("SORU 7 CEVAP")
print(df.sort_values("maas"))

# 8. soru
print("SORU 8 CEVAP")
print(df.sort_values("maas", ascending=False))

# 9. soru
print("SORU 9 CEVAP")
print(df.groupby("sehir")["maas"].mean())

# 10. soru
df["yillik_maas"] = df["maas"] * 12

print("SORU 10 CEVAP")
print(df)

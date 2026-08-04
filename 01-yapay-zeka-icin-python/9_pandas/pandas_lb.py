import pandas as pd

#tablo seklınde verı olusturmak, veri duzenleme, dosyalardan veri okuma


data = [10, 20, 30, 40]
s = pd.Series(data)

print("Pandas Sürümü:", pd.__version__)
print("\nOluşturulan Series:")
print(s)

# series
veri = pd.Series([10, 20, 30, 40])
print(veri)

# series icindeki verilere erisme
veri = pd.Series([10, 20, 30, 40])
print(veri[0])
print(veri[2])

#series icin ozel indeks belirleme
veri = pd.Series([10, 20, 30], index = ["a", "b", "c"])
print(veri)

#dictionary ile series olusturma
veri = {
    "ali": 80,
    "ayşe": 90,
    "mehmet": 75
}

s = pd.Series(veri)
print(s)


#series ozellikleri

print(s.index)
print(s.values)
print(s.dtype)

# series ile matematiksel islemler
veri = pd.Series([10, 20, 30, 40])
sonuc = veri * 2
print(sonuc)

# series filtreleme
yas = pd.Series([10, 20, 30, 40, 50])
filtre = yas > 25
print(filtre)  # true false

sonuc = yas[filtre]
print(sonuc)

# dataframe olusturma

veri = {
    "isim": ["ali", "ayse", "mehmet"],
    "yas": [25, 30, 28],
    "sehir": ["Ankara", "İstanbul", "İzmir"]
}

df = pd.DataFrame(veri)
print(df)

# sutun isimleri
print(df.columns)

# dataframe satır sayısı ogrenme
print(df.shape)

# sutunlara erisim
print(df["isim"])

# birden fazla sutun secme
print(df[["isim", "yas"]])

# yeni sutun ekleme
df["maas"] = [5000, 7000, 6000]
print(df)

# sutun silme
df = df.drop("sehir", axis = 1)
print(df)

# ilk satırları goruntulemek
print(df.head())

# son satırları goruntulemek
print(df.tail())

# dataframe hakkında bilgi
print(df.info())

## dosya okuma ve yazma csv
df = pd.read_csv("veri.csv")
print(df)

## excel okuma
df = pd.read_excel("excel_veri.xlsx")
print(df)

# csv dosyayı yazma
veri = {
    "isim": ["ali", "ayse", "mehmet"],
    "yas": [25, 30, 35]
}

df = pd.DataFrame(veri)

df.to_csv("veri_output.csv", index=False)

# excel dosyası yazma
df.to_excel("veri_output.xlsx", index=False)

# ornek data frame olustur
veri = {
    "isim": ["ali", "ayse", "mehmet", "zeynep", "ahmet"],
    "yas": [25, 30, 28, 35, 22],
    "sehir": ["Ankara", "İstanbul", "İzmir", "Ankara", "Bursa"],
    "maas": [5000, 7000, 6000, 8000, 4500]
}
df = pd.DataFrame(veri)
print(df)

# sütun seçme
print(df["isim"])

# birden fazla sütun seçme
print(df[["isim", "maas"]])

# satır seçme: iloc
print(df.iloc[0])

# birden fazla satır
print(df.iloc[0:3])

# satır seçme: loc
print(df.loc[2])

# belirli bir satır ve belirli bir sütun
print(df.loc[:, ["isim", "maas"]])

print(df.loc[:2, ["isim", "maas"]])

# koşullu filtreleme
filtre = df["yas"] > 30
print(filtre)

sonuc = df[filtre]
print(sonuc)

print(df[df["yas"] > 30])

# birden fazla koşul varsa
sonuc = df[(df["sehir"] == "Ankara") & (df["maas"] > 6000)]
print(sonuc)

# belirli bir değeri içeren satılar
print(df[df["sehir"] == "Ankara"])

# sadece belirli sütunları gösterme
# yaşı 25 den büyük olan verinin sadece isim ve maaşını göster
print(df[df["yas"] > 25][["isim", "maas"]])

# dataframe oluştur
veri = {
    "isim": ["ali", "ayse", "mehmet"],
    "yas": [25, 30, 28],
    "maas": [5000, 7000, 6000]
}

df = pd.DataFrame(veri)
print(df)

# yeni bir sütun ekleme
df["sehir"] = ["Ankara", "İstanbul", "İzmir"]
print(df)

# hesaplama ile sütun oluşturma
df["yillik_maas"] = df["maas"] * 12 
print(df)

# sütun silme
df = df.drop("maas", axis = 1)
print(df)

# sütun isim değiştirme
df = df.rename(columns={"yillik_maas": "yillikMaas"})
print(df)

# yeni satır eklemek
df.loc[3] = ["Zeynep", 32, "Ankara", 80000]
print(df)

# satır silme
df = df.drop(0)
print(df)

# index değerlerini yeniden düzenleme
df = df.reset_index(drop = True)
print(df)


# örnek data frame oluştur
veri = {
    "isim": ["ali", "ayse", "mehmet", "zeynep", "ahmet"],
    "sehir": ["Ankara", "İstanbul", "Ankara", "İzmir", "İstanbul"],
    "maas": [5000, 7000, 6000, 8000, 4500]
}

df = pd.DataFrame(veri)
print(df)

# veri sıralama
df_sirali = df.sort_values("maas")
print(df_sirali)


# azalan sıralama
df_sirali = df.sort_values("maas", ascending=False)
print(df_sirali)

# birden fazla sütuna göre sıralama
df_sirali = df.sort_values(["sehir", "maas"])
print(df_sirali)

# veri gruplama: groupby
gruplar = df.groupby("sehir")
print(gruplar) 

# grupların ortalama maaşı
sonuc = df.groupby("sehir")["maas"].mean() # şehir bazında ortalama maaş hesaplama
print(sonuc)

# grupların toplam maaşı
sonuc = df.groupby("sehir")["maas"].sum()
print(sonuc)

# grupların kaç kişi olduğunu bulalım
sonuc = df.groupby("sehir")["isim"].count()
print(sonuc)

# birden fazla işlem yapma
sonuc = df.groupby("sehir")["maas"].agg(["mean", "max", "min"])
print(sonuc)

# örnek dataframe oluşturalım
veri = {
    "isim": ["ali", "ayse", "mehmet", "zeynep", "ahmet"],
    "yas": [25, 30, 28, 35, 22],
    "sehir": ["Ankara", "İstanbul", "Ankara", "İzmir", "İstanbul"],
    "maas": [5000, 7000, 6000, 8000, 4500]
}

df = pd.DataFrame(veri)
print(df)

# head fonksiyonu ile ilk 5 satırı görelim
print(df.head())

# tail ile son satırları görme
print(df.tail(3))

# info()
print(df.info())

# sayısal sütunların temel istatistiklerini görmek için describe()
print(df.describe())

# bir sütunda ki değerlerin kaç kez tekrar ettiğini görmek için value_counts()
print(df["sehir"].value_counts())

# bir sütunda ki benzersiz değerleri görmek için unique fonksiyonunu kullanırız
print(df["sehir"].unique()) 

# bir sütunda kaç farklı değer olduğunu görmek için nunique
print(df["sehir"].nunique())


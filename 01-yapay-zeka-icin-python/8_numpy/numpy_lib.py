# Yuksek performans, sayısal hesap
# büyük veri, hızlı matematik, matris

import numpy as np

sayilar = [1, 2, 3, 4]
print(sayilar)

dizi = np.array(sayilar)
print(dizi)

print(type(dizi))

print(dizi.shape)

print(dizi.dtype)

dizi = np.zeros(4)
print(dizi)

dizi = np.ones(5)
print(dizi)

dizi = np.arange(0, 10) #belli aralıklarla sayı
print(dizi)

dizi = np.linspace(0, 10, 5) #belli aralıklarla eşit bölünmüs diziler
print(dizi)

# "" matematiksel islemler ""

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

sonuc = a + b
print(sonuc)

sonuc = a - b
print(sonuc)

sonuc = a*b
print(sonuc)

sonuc = a/b
print(sonuc)

a = np.array([1, 2, 3])
sonuc = a*2
print(sonuc)

a = np.array([1, 2, 3, 4])
sonuc = a**2
print(sonuc)

a = np.array([1, 4, 9, 16])
sonuc = np.sqrt(a)
print(sonuc)

a = np.array([1, 2, 3, 4]) #dizi toplamı bulma
print(np.sum(a))

#ortalama
print(np.mean(a))

print(np.max(a))
print(np.min(a))

#standart sapma
print(np.std(a))

#### indeksleme dilimleme 

dizi = np.array([10, 20, 30, 40, 50])
print(dizi[0])

# negatif indeksleme
print(dizi[-1]) #50 gelıyo son eleman

# slicing dilimleme
print(dizi[1:4]) # 1den basla 4 dahil degil (pandasta dahil olacak)

# bastan dilimleme
print(dizi[:3])

#sondan dilim
print(dizi[2:])

# adım(step) kullanımı
print(dizi[::2]) #diziden ikiser adım ile eleman secmek

# 2 boyutlu dizilerde indeksleme
matris = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(matris)

print(matris)

print(matris[0,0]) 

#tüm satır 
print(matris[1, :])

#belirli sutunu cekmek
print(matris[:, 2])

#matris dilimleme
print(matris[0:2, 0:2])

### DİZİ BİRLESTİRME BOLME

#dizi birlestirme

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

sonuc = np.concatenate((a,b))
print(sonuc)

# iki boyutlu dizi birlestirme

a = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)

b = np.array(
    [  
        [5, 6],
        [7, 8]
    ]
)

sonuc = np.concatenate((a, b))
print(sonuc)
## [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# axis parametresi
# axis = 0 ===> satır yonunde birlestirir
# axis = 1 ===> sutun yonunde birlestirir

sonuc = np.concatenate((a,b), axis = 1)
print(sonuc)

# vstack dikey birlestirme
sonuc = np.vstack((a,b))
print(sonuc)

# hstack yatay birlestirme
sonuc = np.hstack((a,b))
print(sonuc)

#### DIZIYI PARCALARA BOLME
dizi = np.array([1,2,3,4,5,6])

sonuc = np.split(dizi, 2)
print(sonuc)

sonuc = np.split(dizi, 3)
print(sonuc)

# İKİ BOYUTLU DİZİLERDE BÖLME
matris = np.array(
    [
        [1,2],
        [3,4],
        [5,6],
        [7,8]
    ]
)

sonuc = np.split(matris, 2)
print(sonuc)

### COK BOYUTLU DIZILER

# iki boyutlu dizi olusturma
matris = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(matris)

# dizi boyutunu ogrenme
print(matris.shape) # (3,3)

# dizinin kac boyutlu oldugunu ogrenme
print(matris.ndim) #2

#dizideki eleman sayısı
print(matris.size) #9

# 3 boyutlu dizi olusturma
dizi3 = np.array(
    [   
        [
            [1,2],
            [3,4]
        ],
        [
            [5,6],
            [7,8]
        ]
    ]
)
print(dizi3)

print(dizi3.shape) # 2 adet matris her matriste 2 satir 

#numpy ile cok boyutlu dizi olusturma
dizi = np.arange(12)
print(dizi)

# matrise donusturme
matris = dizi.reshape(3, 4)
print(matris)

#### MATRIS ISLEMLERI
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])
print(a)
print(b)

print(a + b)
print(a - b)

# gercek matris carpımı
sonuc = np.dot(a, b)
print(sonuc)

# matris transpose (matrisin ters cevrilmesi)
print(a.T) # [[1 3]
           #  [2 4]]

# matris determinant
det = np.linalg.det(a)
print(det)

# matrisin tersi
ters = np.linalg.inv(a)
print(ters)

### NUMPY RASTGELE SAYI URETIMI
# rastgele ondalık sayılar uretme
rastgele = np.random.rand(5)
print(rastgele)

# rastgele matris olusturma
rastgele = np.random.rand(3, 3)
print(rastgele)

# rastgele tam sayı uretme
rastgele = np.random.randint(1, 10, 5)
print(rastgele)

# rastgele tam sayı matrisi uretme
rastgele = np.random.randint(1, 20, (3, 4))
print(rastgele)

# aynı rastgele sonucu uretmek icin (seed)

np.random.seed(42)
rastgele = np.random.rand(5)
print(rastgele)

# bir diziden rastgele eleman secmek
dizi = np.array([10, 20, 30, 40, 50])
secim = np.random.choice(dizi)
print(secim)

# birden fazla eleman secme
secim = np.random.choice(dizi)
print(secim)
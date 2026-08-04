import numpy as np

#1. SORU

dizi = np.arange(1, 21)
print("Dizi:", dizi)
print("Eleman Sayısı:", dizi.size)

#2. SORU

dizi = np.array([5, 10, 15, 20, 25])
sonuc = dizi * 3
print("Sonuç:", sonuc)

# 3. soru

dizi = np.arange(0, 31)
secim = dizi[10:21]
print("Secilenler:", secim)

# 4. soru

a = np.array([1,2,3])
b = np.array([4,5,6])

birlesmis = np.concatenate((a,b))
print("Birleşmiş dizi:", birlesmis)

# 5. soru

dizi = np.arange(1,13)
matris = dizi.reshape(3,4)

print("Matris:\n", matris)
print("Shape:", matris.shape)

# 6.soru

matris = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("İkinci satır:", matris[1])
print("İkinci sütun:", matris[:,1])

# 7. soru

matris = np.random.rand(3,3)

print("Matris:\n", matris)
print("Ortalama:", np.mean(matris))
print("Max:", np.max(matris))

# 8. soru

a = np.array([2,4,6,8])
b = np.array([1,3,5,7])

sonuc = a * b
print("Çarpım sonucu:", sonuc)

# 9. soru

dizi = np.arange(1,10)
matris = dizi.reshape(3,3)

transpose = matris.T

print("Matris:\n", matris)
print("Transpose:\n", transpose)

# 10. soru

sayilar = np.random.randint(1,51,10)

print("Rastgele sayılar:", sayilar)
print("Toplam:", np.sum(sayilar))
print("Ortalama:", np.mean(sayilar))
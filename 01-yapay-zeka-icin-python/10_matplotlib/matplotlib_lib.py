# gorsellestirmeler grafikler

import matplotlib.pyplot as plt

# plt.plot([1, 2, 3], [4, 5, 6])
# plt.show()

# çizgi grafiği olusturma
gunler = [1, 2, 3, 4, 5]
sicaklik = [22, 24, 23, 25, 27]

plt.plot(gunler, sicaklik, color = "red", linestyle = "--", marker = "o")
plt.title("Günlere Göre Sıcaklık") # grafik başlığı
plt.xlabel("Günler") # x ekseni etiketi
plt.ylabel("Sıcaklık") # y ekseni etiketi
plt.grid(True)
plt.show()

# sutun grafikleri

isimler = ["ali", "ayse", "mehmet", "zeynep"]
notlar = [70, 85, 60, 90]

# plt.bar = sütun grafiği oluşturmak için
renkler = ["red", "blue", "green", "orange"]
plt.bar(isimler, notlar, color = renkler)
plt.title("Öğrenci Notları")
plt.xlabel("Öğrenciler")
plt.ylabel("Notlar")
plt.show()

# yatay sütun grafiği
plt.barh(isimler, notlar)
plt.show()

# pie chart pasta dilimi
# plt.pie = pasta grafiği
# değerler = pasta dilimlerinin büyüklüğü
# labels = her dilimin etiketi
# %1.1f%% = yüzdeyi 1 basamaklı ondalık ile gösterir

etiketler = ["python", "java", "c++", "javascript"]
degerler = [40, 25, 20, 15]

ayrim = [0.1, 0, 0, 0]
renkler = ["red", "blue", "green", "orange"]
plt.pie(degerler, labels = etiketler, explode = ayrim, autopct="%1.1f%%", colors = renkler)
plt.title("Programlama Dili Kullanımı")
plt.show()

# scatter plot (dağılım grafigi)
# s nokta boyutu
calisma_saatleri = [1, 2, 3, 4, 5, 6]
notlar = [50, 55, 65, 70, 80, 90]
plt.scatter(calisma_saatleri, notlar, color = "red", s = 100)
plt.title("Çalışma Süresi ve Sınav Notu")
plt.xlabel("Çalışma Saatleri")
plt.ylabel("Notlar")
plt.show()

# birden fazla veri grubu çizdirme

# fen sonuçları
x1 = [1, 2, 3, 4]
y1 = [50, 60, 70, 80]

# mat sonuçları
x2 = [1, 2, 3, 4]
y2 = [55, 65, 75, 85]

plt.scatter(x1, x2, color ="blue", label = "fen")
plt.scatter(x2, y2, color = "red", label = "mat")
plt.legend()
plt.show()

# subplots [birden fazla grafigi aynı anda gosterme]

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

plt.subplot(1, 2, 1) # plt.subplot(satır, sütun, grafik numarası)
plt.plot(x, y1)
plt.title("Grafik 1")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Grafik 2")

plt.show()

# farklı grafik türleri kullanarak subplot oluşturma
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Line Plot")

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("Bar Chart")

plt.show()

# 2x2 grafik oluşturma
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Grafik 1")

plt.subplot(2, 2, 2)
plt.bar(x, y)
plt.title("Grafik 2")

plt.subplot(2, 2, 3)
plt.scatter(x, y)
plt.title("Grafik 3")

plt.subplot(2, 2, 4)
plt.pie(y)
plt.title("Grafik 4")

plt.show()
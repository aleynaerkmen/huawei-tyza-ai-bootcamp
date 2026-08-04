# 1.soru

print("SORU 1")
plt.plot(aylar, satislar)
plt.title("Aylara Göre Satışlar")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
plt.show()

# 2. soru

print("SORU 2")
plt.plot(aylar, karlar, color="red")
plt.title("Aylara Göre Kar")
plt.xlabel("Aylar")
plt.ylabel("Kar")
plt.show()

# 3. soru

print("SORU 3")
plt.plot(aylar, satislar, marker="o")
plt.title("Aylara Göre Satışlar")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
plt.show()

# 4. soru

print("SORU 4")
plt.bar(aylar, satislar)
plt.title("Aylara Göre Satışlar")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
plt.show()

# 5. soru

print("SORU 5")
plt.bar(aylar, reklam, color="green")
plt.title("Aylara Göre Reklam Harcaması")
plt.xlabel("Aylar")
plt.ylabel("Reklam")
plt.show()

# 6. soru

print("SORU 6")
plt.pie(satislar, labels=aylar, autopct="%1.1f%%")
plt.title("Satışların Aylara Göre Dağılımı")
plt.axis("equal")
plt.show()

# 7. soru

print("SORU 7")
plt.scatter(reklam, satislar)
plt.title("Reklam ve Satış İlişkisi")
plt.xlabel("Reklam Harcaması")
plt.ylabel("Satışlar")
plt.show()

# 8. soru

print("SORU 8")
plt.scatter(reklam, karlar, color="red", s=100)
plt.title("Reklam ve Kar İlişkisi")
plt.xlabel("Reklam Harcaması")
plt.ylabel("Kar")
plt.show()

# 9. soru

print("SORU 9")
plt.subplot(1, 2, 1)
plt.plot(aylar, satislar, marker="o")
plt.title("Satışlar")

plt.subplot(1, 2, 2)
plt.bar(aylar, karlar, color="orange")
plt.title("Karlar")

plt.show()


# 10. soru

print("SORU 10")
plt.subplot(2, 2, 1)
plt.plot(aylar, satislar, marker="o")
plt.title("Satışlar")

plt.subplot(2, 2, 2)
plt.bar(aylar, karlar, color="green")
plt.title("Karlar")

plt.subplot(2, 2, 3)
plt.scatter(reklam, satislar, color="red")
plt.title("Reklam-Satış")

plt.subplot(2, 2, 4)
plt.pie(satislar, labels=aylar, autopct="%1.1f%%")
plt.title("Satış Dağılımı")

plt.tight_layout()
plt.show()
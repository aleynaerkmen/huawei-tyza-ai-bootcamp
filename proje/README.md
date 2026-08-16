# 💳 Kredi Kartı Temerrüt ve Risk Tahmini (Credit Card Default Prediction)

Bu proje, **UCI Default of Credit Card Clients** veri seti kullanılarak müşterilerin kredi kartı geri ödeme davranışlarını modellemek, temerrüt (ödememe) riskini tahmin etmek ve risk yönetiminde kritik değişkenleri belirlemek amacıyla geliştirilmiştir.

---

## 📁 Proje Dosyaları

- `AleynaErkmen_credit_card_default_prediction.ipynb`: Veri ön işleme, Keşifçi Veri Analizi (EDA), model eğitimi ve değerlendirme adımlarını içeren colab.
- `default of credit card clients.csv`: Analizde kullanılan 30.000 satırlık müşteri veri seti.

---

## 🛠️ Kullanılan Teknolojiler & Kütüphaneler

- **Dil:** Python
- **Veri Analizi & Manipülasyon:** Pandas, NumPy
- **Görselleştirme:** Matplotlib, Seaborn
- **Makine Öğrenmesi:** Scikit-Learn (LogisticRegression, RandomForestClassifier, StandardScaler, ROC-AUC)

---

## 📊 Model Karşılaştırması ve Bulgular

Verideki sınıf dengesizliği (%78 düzenli ödeyen, %22 geciktiren) göz önüne alınarak modeller Accuracy, Confusion Matrix ve ROC-AUC metrikleriyle değerlendirilmiştir:

| Model | Doğruluk (Accuracy) | ROC-AUC Skoru |
| :--- | :--- | :--- |
| **Lojistik Regresyon** | %81.18 | 0.72 |
| **Random Forest** | **%81.65** | **0.78** |

### 🔍 Önemli Çıkarımlar (Feature Importance):
1. **Gecikme Geçmişi:** `PAY_0` (son ay gecikme durumu) ve `PAY_2`, temerrüt riskini belirleyen en baskın değişkenlerdir.
2. **Kredi Limiti:** Düşük `LIMIT_BAL` değerine sahip müşterilerde temerrüt riski belirgin şekilde daha yüksektir.
3. **Davranış Önceliği:** Dinamik ödeme alışkanlıkları, statik demografik özelliklere kıyasla model performansında çok daha belirleyicidir.

---

## 📝 Medium Yazısı
Projenin detaylı analizine, iş çıkarımlarına ve görselleştirmelerine Medium üzerinden ulaşabilirsiniz:
👉 https://medium.com/@aleynaerkmen/makine-%C3%B6%C4%9Frenmesi-ile-kredi-kart%C4%B1-temerr%C3%BCt-default-tahmini-6f77641ce0ab

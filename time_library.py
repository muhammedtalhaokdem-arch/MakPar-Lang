import datetime
import os

# 1. Klasör yollarını bul
kutuphane_klasoru = os.path.dirname(os.path.abspath(__file__)) 
ana_klasor = os.path.dirname(kutuphane_klasoru)                
veri_klasoru = os.path.join(ana_klasor, "Library-Data")        

# 2. Library-Data klasörü yoksa otomatik oluştur
if not os.path.exists(veri_klasoru):
    os.makedirs(veri_klasoru)

# 3. Dosyanın kaydedileceği tam yol
sonuc_yolu = os.path.join(veri_klasoru, "time.txt")

# 4. SADECE SAAT VE DAKİKAYI AL (Tarih ve saniye çıkarıldı)
tam_tarih = datetime.datetime.now().strftime("%H:%M")

with open(sonuc_yolu, "w", encoding="utf-8") as dosya:
    dosya.write(tam_tarih)
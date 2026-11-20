import datetime
import os

# 1. Klasör yollarını bul
kutuphane_klasoru = os.path.dirname(os.path.abspath(__file__))
ana_klasor = os.path.dirname(kutuphane_klasoru)
veri_klasoru = os.path.join(ana_klasor, "Library-Data")

# Library-Data yoksa oluştur (güvenlik)
if not os.path.exists(veri_klasoru):
    os.makedirs(veri_klasoru)

# 2. Yazılacak dosyanın tam yolu
sonuc_yolu = os.path.join(veri_klasoru, "date_full.txt")

try:
    # 3. Tarih verisini üret ve dosyaya yaz
    tam_tarih = datetime.datetime.now().strftime("%d.%m.%Y")
    
    with open(sonuc_yolu, "w", encoding="utf-8") as f:
        f.write(tam_tarih)
        
except Exception as e:
    with open(sonuc_yolu, "w", encoding="utf-8") as f:
        f.write("HATA_TARIH_ALINAMADI")

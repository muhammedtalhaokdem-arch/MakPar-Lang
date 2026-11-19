import random
import os

# 1. Klasör yollarını bul
kutuphane_klasoru = os.path.dirname(os.path.abspath(__file__))
ana_klasor = os.path.dirname(kutuphane_klasoru)
veri_klasoru = os.path.join(ana_klasor, "Library-Data")

# Library-Data yoksa oluştur (güvenlik)
if not os.path.exists(veri_klasoru):
    os.makedirs(veri_klasoru)

# 2. Okunacak ve yazılacak dosyaların tam yolları
min_yolu = os.path.join(veri_klasoru, "Min.txt")
max_yolu = os.path.join(veri_klasoru, "MAX.txt")
sonuc_yolu = os.path.join(veri_klasoru, "Random.txt")

try:
    # 3. MakPar'ın bıraktığı Min ve Max değerlerini oku
    with open(min_yolu, "r", encoding="utf-8") as f:
        min_deger = int(f.read().strip())
        
    with open(max_yolu, "r", encoding="utf-8") as f:
        max_deger = int(f.read().strip())
        
    # Güvenlik önlemi: Eğer Min yanlışlıkla Max'tan büyük yazıldıysa yer değiştir
    if min_deger > max_deger:
        min_deger, max_deger = max_deger, min_deger
        
    # 4. Rastgele sayıyı üret
    uretilen_sayi = random.randint(min_deger, max_deger)
    
    # 5. Sonucu Random.txt dosyasına yaz
    with open(sonuc_yolu, "w", encoding="utf-8") as f:
        f.write(str(uretilen_sayi))
        
except Exception as e:
    # Eğer dosyalar eksikse veya içine sayı yerine harf yazılmışsa motoru çökertmemek için hata mesajı yaz
    with open(sonuc_yolu, "w", encoding="utf-8") as f:
        f.write("HATA_GECERSIZ_SAYI")
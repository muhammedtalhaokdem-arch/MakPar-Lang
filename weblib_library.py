import webbrowser
import os

# 1. Klasör yollarını bul
kutuphane_klasoru = os.path.dirname(os.path.abspath(__file__))
ana_klasor = os.path.dirname(kutuphane_klasoru)
veri_klasoru = os.path.join(ana_klasor, "Library-Data")

# 2. Sadece istek.txt dosyasının yolunu belirle
istek_yolu = os.path.join(veri_klasoru, "istek.txt")

try:
    # 3. MakPar'ın istek.txt içine yazdığı linki oku
    with open(istek_yolu, "r", encoding="utf-8") as f:
        url = f.read().strip()
    
    # 4. Eğer dosya boş değilse, o linki bilgisayarın tarayıcısında aç
    if url:
        webbrowser.open(url)
        
except Exception:
    pass # Dosya yoksa veya hatalıysa motoru durdurmamak için sessizce kapan